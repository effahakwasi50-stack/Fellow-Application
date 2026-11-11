import React, { useRef, useState } from 'react';
import { RepublicHallCrest } from './RepublicHallCrest.tsx';
import { UploadCloud, RotateCcw, Shield, Check } from 'lucide-react';

interface HeaderProps {
  customLogoUrl: string | null;
  onUploadLogo: (url: string | null) => void;
}

export const Header: React.FC<HeaderProps> = ({
  customLogoUrl,
  onUploadLogo,
}) => {
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const [showUploader, setShowUploader] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const result = event.target?.result as string;
      if (result) {
        onUploadLogo(result);
        setShowUploader(false);
      }
    };
    reader.readAsDataURL(file);
  };

  const handleResetLogo = () => {
    onUploadLogo(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
    setShowUploader(false);
  };

  return (
    <header className="no-print bg-[#0b6623] text-white shadow-md border-b-4 border-[#d4af37]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 sm:py-4">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
          {/* Brand Info with Official Crest */}
          <div className="flex items-center gap-3.5 sm:gap-4">
            <div className="relative group shrink-0">
              {customLogoUrl ? (
                <img
                  src={customLogoUrl}
                  alt="Republic Hall Crest"
                  className="w-14 h-14 sm:w-16 sm:h-16 rounded-full object-contain bg-white/95 p-1 border-2 border-[#d4af37] shadow-sm"
                />
              ) : (
                <RepublicHallCrest
                  size={58}
                  className="w-14 h-14 sm:w-16 sm:h-16 drop-shadow-md"
                />
              )}
            </div>

            <div className="space-y-0.5">
              <div className="flex items-center gap-2">
                <span className="text-[10px] sm:text-xs font-semibold tracking-widest text-[#d4af37] uppercase">
                  KWAME NKRUMAH UNIVERSITY OF SCIENCE &amp; TECHNOLOGY, KUMASI
                </span>
              </div>
              <h1 className="text-xl sm:text-2xl font-black tracking-tight text-white flex items-center gap-2">
                REPUBLIC HALL
                <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-[#d4af37] text-[#084c1a] tracking-normal uppercase hidden sm:inline-block">
                  Set The Pace
                </span>
              </h1>
              <div className="text-xs sm:text-sm font-medium text-emerald-100 flex items-center gap-2">
                <span>Fellow Application Portal</span>
                <span className="text-emerald-300">•</span>
                <span className="text-emerald-200 text-xs">Official Portal</span>
              </div>
            </div>
          </div>

          {/* Crest Customization and Security Badge */}
          <div className="flex items-center gap-2 self-start md:self-center">
            <div className="relative">
              <button
                type="button"
                onClick={() => setShowUploader(!showUploader)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold bg-emerald-900/60 hover:bg-emerald-900 text-emerald-100 hover:text-white rounded-lg border border-emerald-700/60 transition-colors shadow-xs"
                aria-label="Crest options and logo uploader"
              >
                <UploadCloud className="w-3.5 h-3.5 text-[#d4af37]" />
                <span>{customLogoUrl ? 'Custom Crest Active' : 'Crest Options'}</span>
              </button>

              {/* Popover */}
              {showUploader && (
                <div className="absolute right-0 mt-2 w-72 bg-white text-slate-800 rounded-xl shadow-xl border border-slate-200 p-4 z-50 space-y-3">
                  <div className="flex items-center justify-between pb-2 border-b border-slate-100">
                    <span className="text-xs font-bold text-slate-800">
                      Hall Crest Options
                    </span>
                    <button
                      type="button"
                      onClick={() => setShowUploader(false)}
                      className="text-slate-400 hover:text-slate-600 text-xs"
                    >
                      ✕
                    </button>
                  </div>

                  <p className="text-[11px] text-slate-500">
                    The portal uses the official vector Republic Hall crest by default. You can upload a custom seal if needed.
                  </p>

                  <div className="space-y-2">
                    <input
                      ref={fileInputRef}
                      type="file"
                      id="crest-file-upload"
                      accept="image/png, image/jpeg, image/svg+xml"
                      onChange={handleFileChange}
                      className="hidden"
                    />
                    <label
                      htmlFor="crest-file-upload"
                      className="w-full flex items-center justify-center gap-2 py-2 px-3 bg-[#0b6623] hover:bg-[#084c1a] text-white rounded-lg text-xs font-semibold cursor-pointer transition-colors"
                    >
                      <UploadCloud className="w-4 h-4 text-[#d4af37]" />
                      Upload Crest Image
                    </label>

                    {customLogoUrl && (
                      <button
                        type="button"
                        onClick={handleResetLogo}
                        className="w-full flex items-center justify-center gap-1.5 py-1.5 px-3 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-medium transition-colors"
                      >
                        <RotateCcw className="w-3.5 h-3.5" />
                        Reset to Official Crest
                      </button>
                    )}
                  </div>
                </div>
              )}
            </div>

            <div className="hidden lg:flex items-center gap-1 text-[11px] text-emerald-200 bg-emerald-950/40 px-2.5 py-1.5 rounded-lg border border-emerald-800/40">
              <Shield className="w-3.5 h-3.5 text-[#d4af37]" />
              <span>100% Client-Side &amp; Private</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
