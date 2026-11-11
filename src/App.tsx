import React, { useState } from 'react';
import { Header } from './components/Header.tsx';
import { ApplicationForm } from './components/ApplicationForm.tsx';
import { LetterPreview } from './components/LetterPreview.tsx';
import { ExportControls } from './components/ExportControls.tsx';
import {
  FellowFormData,
  getDefaultFormData,
  validateApplication,
} from './utils/formValidation.ts';

export default function App() {
  const [formData, setFormData] = useState<FellowFormData>(getDefaultFormData());
  const [customLogoUrl, setCustomLogoUrl] = useState<string | null>(null);
  const [showLetterheadCrest, setShowLetterheadCrest] = useState<boolean>(false);

  // Real-time validation
  const validation = validateApplication(formData);

  const handleFormChange = (updated: Partial<FellowFormData>) => {
    setFormData((prev) => ({
      ...prev,
      ...updated,
    }));
  };

  const handleResetSample = () => {
    setFormData(getDefaultFormData());
  };

  const handleClearAll = () => {
    setFormData({
      fullName: '',
      collegeDept: '',
      phoneNumber: '',
      email: '',
      applicationDate: '',
      signatureDataUrl: '',
    });
  };

  return (
    <div className="min-h-screen bg-[#f8fafc] flex flex-col text-slate-800">
      {/* Portal Header */}
      <Header
        customLogoUrl={customLogoUrl}
        onUploadLogo={(url) => setCustomLogoUrl(url)}
      />

      {/* Main Split-Screen Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Left Column: Applicant Form & Signature Controls */}
          <div className="no-print lg:col-span-5 space-y-4">
            <ApplicationForm
              formData={formData}
              onChange={handleFormChange}
              errors={validation.errors}
              onResetSample={handleResetSample}
              onClearAll={handleClearAll}
            />
          </div>

          {/* Right Column: Action Buttons & Live A4 Letter Preview */}
          <div className="lg:col-span-7 flex flex-col items-center">
            <div className="w-full">
              {/* Export and Print Controls placed right above preview */}
              <ExportControls
                isValid={validation.isValid}
                missingFields={validation.missingFields}
                formData={formData}
                showLetterheadCrest={showLetterheadCrest}
                onToggleCrest={(val) => setShowLetterheadCrest(val)}
              />

              {/* Live A4 Letter Preview */}
              <LetterPreview
                formData={formData}
                customLogoUrl={customLogoUrl}
                showLetterheadCrest={showLetterheadCrest}
              />
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="no-print bg-slate-900 text-slate-400 border-t border-slate-800 text-xs py-4 text-center">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <div>
            &copy; {new Date().getFullYear()} Republic Hall, Kwame Nkrumah University of Science and Technology (KNUST).
          </div>
          <div className="flex items-center gap-3 text-slate-400">
            <span className="text-[#d4af37] font-semibold">Set The Pace</span>
            <span>•</span>
            <span>Hall Warden&apos;s Secretariat</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
