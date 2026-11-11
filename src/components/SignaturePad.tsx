import React, { useRef, useState, useEffect, useCallback } from 'react';
import { PenTool, RotateCcw, CheckCircle } from 'lucide-react';

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
  const [inkColor, setInkColor] = useState<'#000080' | '#111111'>('#000080');
  const [isDrawing, setIsDrawing] = useState(false);
  const [hasDrawnStroke, setHasDrawnStroke] = useState(false);

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
  }, [setupCanvas]);

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

    // Live update signature in real-time as user strokes
    const dataUrl = canvas.toDataURL('image/png');
    onChange(dataUrl);
  };

  const stopDrawing = () => {
    if (!isDrawing) return;
    setIsDrawing(false);
    lastPointRef.current = null;

    const canvas = canvasRef.current;
    if (canvas && hasDrawnStroke) {
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
    onChange('');
  };

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between">
        <label className="block text-sm font-semibold text-slate-800 flex items-center gap-1.5">
          <PenTool className="w-4 h-4 text-[#0b6623]" />
          <span>Live Electronic Signature</span>
          <span className="text-red-600 font-bold">*</span>
        </label>
        {signature ? (
          <span className="inline-flex items-center gap-1 text-xs font-medium text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
            <CheckCircle className="w-3.5 h-3.5 text-emerald-600" />
            Live Signature Captured
          </span>
        ) : (
          <span className="text-xs text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200 font-medium">
            Draw your signature below
          </span>
        )}
      </div>

      {/* Controls bar */}
      <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600 bg-slate-50 p-2 rounded-lg border border-slate-200">
        <div className="flex items-center gap-2">
          <span className="font-semibold text-slate-700">Ink Color:</span>
          <button
            type="button"
            onClick={() => setInkColor('#000080')}
            className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-semibold border transition-all cursor-pointer ${
              inkColor === '#000080'
                ? 'border-[#000080] bg-blue-100/70 text-[#000080] ring-1 ring-[#000080]'
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
            className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded text-xs font-semibold border transition-all cursor-pointer ${
              inkColor === '#111111'
                ? 'border-slate-900 bg-slate-200 text-slate-900 ring-1 ring-slate-900'
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
          className="inline-flex items-center gap-1 px-2.5 py-1 rounded text-xs font-semibold text-rose-700 hover:bg-rose-100/60 bg-white border border-rose-200 transition-colors cursor-pointer"
          aria-label="Clear Signature"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          Clear Signature
        </button>
      </div>

      {/* Live Drawing Canvas Pad */}
      <div className="relative border-2 border-dashed border-slate-300 hover:border-[#0b6623] focus-within:border-[#0b6623] rounded-lg bg-white overflow-hidden shadow-inner">
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
          aria-label="Live signature drawing canvas"
        />
        {/* Guide line */}
        <div className="pointer-events-none absolute bottom-5 left-6 right-6 border-b border-slate-200 flex justify-between items-center text-[10px] text-slate-400 select-none">
          <span>Sign above this line (Draw with Mouse or Touch)</span>
          <span>Republic Hall, KNUST</span>
        </div>
        {!signature && !isDrawing && (
          <div className="pointer-events-none absolute inset-0 flex items-center justify-center text-xs text-slate-400 font-medium">
            ✍️ Click &amp; drag or touch screen here to draw your signature live
          </div>
        )}
      </div>

      {/* Error message */}
      {error && <p className="text-xs text-rose-600 font-medium">{error}</p>}
    </div>
  );
};
