import React, { useState } from 'react';
import html2canvas from 'html2canvas';
import { jsPDF } from 'jspdf';
import {
  Download,
  Printer,
  Loader2,
  AlertCircle,
  CheckCircle,
  FileText,
} from 'lucide-react';
import { FellowFormData, sanitizeFileName } from '../utils/formValidation.ts';

interface ExportControlsProps {
  isValid: boolean;
  missingFields: string[];
  formData: FellowFormData;
  showLetterheadCrest: boolean;
  onToggleCrest: (show: boolean) => void;
}

export const ExportControls: React.FC<ExportControlsProps> = ({
  isValid,
  missingFields,
  formData,
  showLetterheadCrest,
  onToggleCrest,
}) => {
  const [isGenerating, setIsGenerating] = useState(false);
  const [downloadSuccess, setDownloadSuccess] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleDownloadPdf = async () => {
    if (!isValid || isGenerating) return;

    // Clean up any stray offscreen clones first
    const existingClones = document.querySelectorAll('.a4-pdf-clone-temp');
    existingClones.forEach((el) => el.remove());

    try {
      setIsGenerating(true);
      setErrorMessage(null);
      setDownloadSuccess(false);

      const targetEl = document.getElementById('a4-letter-sheet');
      if (!targetEl) {
        throw new Error('A4 letter sheet element not found in DOM.');
      }

      // Create an offscreen clone container at exact desktop 794px width
      // to ensure razor-sharp output even on small mobile screens
      const clone = targetEl.cloneNode(true) as HTMLElement;
      clone.classList.add('a4-pdf-clone-temp');
      clone.style.transform = 'none';
      clone.style.margin = '0';
      clone.style.width = '794px';
      clone.style.minHeight = '1123px';
      clone.style.boxShadow = 'none';
      clone.style.border = 'none';
      clone.style.position = 'fixed';
      clone.style.left = '-9999px';
      clone.style.top = '0';
      clone.style.zIndex = '-1000';
      clone.style.backgroundColor = '#ffffff';

      // Recursively strip any oklch color references in computed styles of cloned tree
      const sanitizeTree = (node: HTMLElement) => {
        const style = node.style;
        if (style.color && style.color.includes('oklch')) style.color = '#111111';
        if (style.backgroundColor && style.backgroundColor.includes('oklch')) style.backgroundColor = '#ffffff';
        if (style.borderColor && style.borderColor.includes('oklch')) style.borderColor = '#e2e8f0';

        Array.from(node.children).forEach((child) => {
          if (child instanceof HTMLElement) sanitizeTree(child);
        });
      };
      sanitizeTree(clone);

      document.body.appendChild(clone);

      // Wait a tick for rendering settling
      await new Promise((resolve) => setTimeout(resolve, 60));

      const canvas = await html2canvas(clone, {
        scale: 2, // 2x high resolution
        useCORS: true,
        allowTaint: true,
        backgroundColor: '#ffffff',
        width: 794,
        windowWidth: 794,
        logging: false,
        onclone: (clonedDoc) => {
          const clonedTarget = clonedDoc.querySelector('.a4-pdf-clone-temp') as HTMLElement;
          if (clonedTarget) {
            clonedTarget.style.display = 'block';
            clonedTarget.style.visibility = 'visible';
            clonedTarget.style.color = '#111111';
            clonedTarget.style.backgroundColor = '#ffffff';
          }
        },
      });

      // Remove offscreen clone
      clone.remove();

      // Create standard A4 PDF (210mm x 297mm)
      const pdf = new jsPDF({
        orientation: 'portrait',
        unit: 'mm',
        format: 'a4',
        compress: true,
      });

      const pdfWidth = pdf.internal.pageSize.getWidth(); // 210
      const pdfHeight = pdf.internal.pageSize.getHeight(); // 297
      const imgData = canvas.toDataURL('image/png', 1.0);

      // Add image filling A4 sheet
      pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight, undefined, 'FAST');

      const fileName = sanitizeFileName(formData.fullName);
      pdf.save(fileName);

      setDownloadSuccess(true);
      setTimeout(() => setDownloadSuccess(false), 4500);
    } catch (err) {
      console.error('PDF Generation failed:', err);
      setErrorMessage('Failed to generate PDF. Please try the Print / Save as PDF button.');
    } finally {
      setIsGenerating(false);
      // Ensure cleanup of any temp elements
      const lingering = document.querySelectorAll('.a4-pdf-clone-temp');
      lingering.forEach((el) => el.remove());
    }
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="no-print space-y-3 mb-4">
      {/* Top Banner & Crest toggle */}
      <div className="flex flex-wrap items-center justify-between gap-2 bg-white/90 p-3 rounded-lg border border-slate-200 shadow-xs">
        <div className="flex items-center gap-2">
          <FileText className="w-4 h-4 text-[#0b6623]" />
          <span className="text-xs font-bold text-slate-800">
            Official Live A4 Letter Preview
          </span>
          <span className="text-[11px] text-slate-500 hidden sm:inline">
            (Times New Roman, 11.5pt, 1.65 line height)
          </span>
        </div>

        {/* Crest display switch */}
        <label className="flex items-center gap-2 text-xs font-medium text-slate-700 cursor-pointer select-none">
          <input
            type="checkbox"
            checked={showLetterheadCrest}
            onChange={(e) => onToggleCrest(e.target.checked)}
            className="rounded border-slate-300 text-[#0b6623] focus:ring-[#0b6623]"
          />
          <span>Include Hall Crest in Letterhead</span>
        </label>
      </div>

      {/* Two Prominent Action Buttons */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        {/* Button 1: Download Completed Application (PDF) */}
        <button
          type="button"
          onClick={handleDownloadPdf}
          disabled={!isValid || isGenerating}
          className={`relative group flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl text-sm font-bold shadow-md transition-all duration-200 ${
            isValid && !isGenerating
              ? 'bg-[#0b6623] hover:bg-[#084c1a] active:bg-[#063a13] text-white hover:shadow-lg cursor-pointer'
              : 'bg-slate-200 text-slate-400 cursor-not-allowed border border-slate-300 shadow-none'
          }`}
          aria-label="Download Completed Application (PDF)"
        >
          {isGenerating ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              <span>Generating Crisp PDF...</span>
            </>
          ) : (
            <>
              <Download className="w-5 h-5 text-[#d4af37] group-hover:scale-110 transition-transform" />
              <span>Download Completed Application (PDF)</span>
            </>
          )}
        </button>

        {/* Button 2: Print / Save as PDF */}
        <button
          type="button"
          onClick={handlePrint}
          className="flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl text-sm font-bold bg-white hover:bg-slate-50 text-slate-800 border-2 border-slate-300 hover:border-slate-400 shadow-xs active:bg-slate-100 transition-all cursor-pointer"
          aria-label="Print / Save as PDF"
        >
          <Printer className="w-5 h-5 text-slate-600" />
          <span>Print / Save as PDF</span>
        </button>
      </div>

      {/* Helpful reminder when disabled */}
      {!isValid && (
        <div className="flex items-start gap-2 p-3 bg-amber-50 border border-amber-200 rounded-lg text-xs text-amber-900">
          <AlertCircle className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
          <div>
            <span className="font-semibold">PDF Download Reminder:</span> Please complete all compulsory fields (*) and provide your electronic signature to enable PDF download. Missing:{' '}
            <span className="font-medium">{missingFields.join(', ')}</span>.
          </div>
        </div>
      )}

      {/* Success alert */}
      {downloadSuccess && (
        <div className="flex items-center gap-2 p-2.5 bg-emerald-50 border border-emerald-200 rounded-lg text-xs text-emerald-800">
          <CheckCircle className="w-4 h-4 text-emerald-600 shrink-0" />
          <span>Application PDF downloaded successfully! Check your browser downloads folder.</span>
        </div>
      )}

      {/* Error alert */}
      {errorMessage && (
        <div className="flex items-center gap-2 p-2.5 bg-red-50 border border-red-200 rounded-lg text-xs text-red-800">
          <AlertCircle className="w-4 h-4 text-red-600 shrink-0" />
          <span>{errorMessage}</span>
        </div>
      )}
    </div>
  );
};
