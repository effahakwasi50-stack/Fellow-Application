import React, { useRef, useState, useEffect, useCallback } from 'react';
import { PenTool, Upload, RotateCcw, CheckCircle, Image as ImageIcon } from 'lucide-react';

interface SignaturePadProps {
  signature: string;
  onChange: (signatureDataUrl: string) => void;
  error?: string;
}

export const SignaturePad: React.FC<SignaturePadProps> = ({
  signature,
  onChange,
  error,
}) => {
  const [activeTab, setActiveTab] = useState<'draw' | 'upload'>('draw');
  const [inkColor, setInkColor] = useState<'#000080' | '#111111'>('#000080');
  const [isDrawing, setIsDrawing] = useState(false);
  const [hasDrawnStroke, setHasDrawnStroke] = useState(false);
  const [uploadFileName, setUploadFileName] = useState<string | null>(null);

  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const lastPointRef = useRef<{ x: number; y: number } | null>(null);

  // Sync canvas with high-DPI scaling
  const setupCanvas = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;

    // Only resize if internal dimensions differ to avoid clearing unintentionally
    if (canvas.width !== Math.floor(rect.width * dpr) || canvas.height !== Math.floor(rect.height * dpr)) {
      canvas.width = Math.floor(rect.width * dpr);
      canvas.height = Math.floor(rect.height * dpr);
      ctx.scale(dpr, dpr);
    }

    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    ctx.strokeStyle = inkColor;
    ctx.lineWidth = 2.2;
  }, [inkColor]);

  useEffect(() => {
    setupCanvas();
  }, [setupCanvas, activeTab]);

  const getCanvasCoordinates = (
    e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>
  ): { x: number; y: number } | null => {
    const canvas = canvasRef.current;
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();

    let clientX = 0;
    let clientY = 0;

    if ('touches' in e) {
      if (e.touches.length === 0) return null;
      clientX = e.touches[0].clientX;
      clientY = e.touches[0].clientY;
    } else {
      clientX = e.clientX;
      clientY = e.clientY;
    }

    return {
      x: clientX - rect.left,
      y: clientY - rect.top,
    };
  };

  const startDrawing = (
    e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>
  ) => {
    // Prevent default touch scrolling
    if ('touches' in e) {
      e.preventDefault();
    }
    const coords = getCanvasCoordinates(e);
    if (!coords) return;

    setIsDrawing(true);
    lastPointRef.current = coords;
  };

  const draw = (
    e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>
  ) => {
    if (!isDrawing || !lastPointRef.current) return;
    if ('touches' in e) {
      e.preventDefault();
    }

    const currentCoords = getCanvasCoordinates(e);
    if (!currentCoords) return;

    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.strokeStyle = inkColor;
    ctx.lineWidth = 2.2;
    ctx.beginPath();
    ctx.moveTo(lastPointRef.current.x, lastPointRef.current.y);
    ctx.lineTo(currentCoords.x, currentCoords.y);
    ctx.stroke();

    lastPointRef.current = currentCoords;
    setHasDrawnStroke(true);
  };

  const stopDrawing = () => {
    if (!isDrawing) return;
    setIsDrawing(false);
    lastPointRef.current = null;

    const canvas = canvasRef.current;
    if (canvas && hasDrawnStroke) {
      // Export transparent PNG
      const dataUrl = canvas.toDataURL('image/png');
      onChange(dataUrl);
    }
  };

  const handleClear = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      if (ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    setHasDrawnStroke(false);
    setUploadFileName(null);
    onChange('');
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.type.startsWith('image/')) {
      alert('Please upload a valid image file (PNG or JPG).');
      return;
    }

    const reader = new FileReader();
    reader.onload = (event) => {
      const result = event.target?.result as string;
      if (result) {
        setUploadFileName(file.name);
        onChange(result);
      }
    };
    reader.readAsDataURL(file);
  };

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between">
        <label className="block text-sm font-semibold text-slate-800">
          Electronic Signature <span className="text-red-600">*</span>
        </label>
        {signature && (
          <span className="inline-flex items-center gap-1 text-xs font-medium text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
            <CheckCircle className="w-3.5 h-3.5 text-emerald-600" />
            Signature Attached
          </span>
        )}
      </div>

      {/* Tabs */}
      <div className="flex border-b border-slate-200 bg-slate-100/70 p-1 rounded-lg">
        <button
          type="button"
          onClick={() => setActiveTab('draw')}
          className={`flex-1 flex items-center justify-center gap-2 py-1.5 px-3 rounded-md text-xs sm:text-sm font-medium transition-all ${
            activeTab === 'draw'
              ? 'bg-white text-[#0b6623] shadow-sm font-semibold'
              : 'text-slate-600 hover:text-slate-900'
          }`}
          aria-label="Draw Signature tab"
        >
          <PenTool className="w-4 h-4" />
          Tab 1: Draw Signature
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('upload')}
          className={`flex-1 flex items-center justify-center gap-2 py-1.5 px-3 rounded-md text-xs sm:text-sm font-medium transition-all ${
            activeTab === 'upload'
              ? 'bg-white text-[#0b6623] shadow-sm font-semibold'
              : 'text-slate-600 hover:text-slate-900'
          }`}
          aria-label="Upload Signature tab"
        >
          <Upload className="w-4 h-4" />
          Tab 2: Upload Signature
        </button>
      </div>

      {/* Tab 1: Draw */}
      {activeTab === 'draw' && (
        <div className="space-y-2">
          {/* Controls bar */}
          <div className="flex items-center justify-between text-xs text-slate-600">
            <div className="flex items-center gap-2">
              <span className="font-medium text-slate-700">Ink Color:</span>
              <button
                type="button"
                onClick={() => setInkColor('#000080')}
                className={`inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-semibold border transition-all ${
                  inkColor === '#000080'
                    ? 'border-[#000080] bg-blue-50 text-[#000080] ring-1 ring-[#000080]'
                    : 'border-slate-300 bg-white text-slate-700 hover:bg-slate-50'
                }`}
                aria-label="Select Blue Ink"
              >
                <span className="w-2.5 h-2.5 rounded-full bg-[#000080]" />
                Blue Ink (#000080)
              </button>
              <button
                type="button"
                onClick={() => setInkColor('#111111')}
                className={`inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-semibold border transition-all ${
                  inkColor === '#111111'
                    ? 'border-slate-900 bg-slate-100 text-slate-900 ring-1 ring-slate-900'
                    : 'border-slate-300 bg-white text-slate-700 hover:bg-slate-50'
                }`}
                aria-label="Select Black Ink"
              >
                <span className="w-2.5 h-2.5 rounded-full bg-[#111111]" />
                Black Ink (#111111)
              </button>
            </div>

            <button
              type="button"
              onClick={handleClear}
              className="inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-medium text-rose-700 hover:bg-rose-50 border border-rose-200 transition-colors"
              aria-label="Clear Signature"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              Clear Signature
            </button>
          </div>

          {/* Canvas Pad */}
          <div className="relative border-2 border-dashed border-slate-300 hover:border-slate-400 focus-within:border-[#0b6623] rounded-lg bg-white overflow-hidden shadow-inner">
            <canvas
              ref={canvasRef}
              className="signature-canvas w-full h-32 block bg-transparent"
              onMouseDown={startDrawing}
              onMouseMove={draw}
              onMouseUp={stopDrawing}
              onMouseLeave={stopDrawing}
              onTouchStart={startDrawing}
              onTouchMove={draw}
              onTouchEnd={stopDrawing}
              aria-label="Signature drawing canvas"
            />
            {/* Guide line */}
            <div className="pointer-events-none absolute bottom-5 left-6 right-6 border-b border-slate-200 flex justify-between items-center text-[10px] text-slate-300 select-none">
              <span>Sign above this line</span>
              <span>Kwame Nkrumah University of Science and Technology</span>
            </div>
            {!signature && !isDrawing && (
              <div className="pointer-events-none absolute inset-0 flex items-center justify-center text-xs text-slate-400">
                Click &amp; drag or touch to sign
              </div>
            )}
          </div>
        </div>
      )}

      {/* Tab 2: Upload */}
      {activeTab === 'upload' && (
        <div className="space-y-2">
          <div className="border-2 border-dashed border-slate-300 rounded-lg p-4 bg-white text-center hover:border-[#0b6623] transition-colors">
            <input
              type="file"
              id="signature-upload"
              accept="image/png, image/jpeg, image/jpg"
              onChange={handleFileUpload}
              className="hidden"
            />
            <label
              htmlFor="signature-upload"
              className="cursor-pointer flex flex-col items-center justify-center space-y-2"
            >
              <div className="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-[#0b6623]">
                <ImageIcon className="w-5 h-5" />
              </div>
              <div className="text-xs text-slate-700">
                <span className="font-semibold text-[#0b6623] hover:underline">
                  Click to browse
                </span>{' '}
                or drag signature image here
              </div>
              <p className="text-[11px] text-slate-500">
                PNG or JPG with transparent or clean white background
              </p>
            </label>
          </div>

          {uploadFileName && (
            <div className="flex items-center justify-between p-2 bg-slate-50 rounded border border-slate-200 text-xs">
              <span className="truncate font-medium text-slate-700">
                File: {uploadFileName}
              </span>
              <button
                type="button"
                onClick={handleClear}
                className="text-rose-600 hover:text-rose-800 text-xs font-semibold ml-2"
              >
                Remove
              </button>
            </div>
          )}
        </div>
      )}

      {/* Error message */}
      {error && <p className="text-xs text-rose-600 font-medium">{error}</p>}
    </div>
  );
};
