import React, { useRef, useEffect, useState } from 'react';
import { FellowFormData } from '../utils/formValidation.ts';
import { RepublicHallCrest } from './RepublicHallCrest.tsx';

interface LetterPreviewProps {
  formData: FellowFormData;
  customLogoUrl?: string | null;
  showLetterheadCrest?: boolean;
}

export const LetterPreview: React.FC<LetterPreviewProps> = ({
  formData,
  customLogoUrl,
  showLetterheadCrest = false,
}) => {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [scaleFactor, setScaleFactor] = useState<number>(1);

  // Auto-scale on mobile so 794px sheet fits viewport without horizontal scrolling or squished words
  useEffect(() => {
    const updateScale = () => {
      if (!containerRef.current) return;
      const containerWidth = containerRef.current.clientWidth;
      const targetWidth = 794; // Standard A4 desktop width at 96dpi

      if (containerWidth < targetWidth + 16) {
        // Reserve small padding around sheet
        const available = Math.max(containerWidth - 16, 280);
        setScaleFactor(available / targetWidth);
      } else {
        setScaleFactor(1);
      }
    };

    updateScale();
    window.addEventListener('resize', updateScale);
    return () => window.removeEventListener('resize', updateScale);
  }, []);

  // Format fallbacks for unfilled inputs
  const displayDate = formData.applicationDate.trim() || '[Application Date]';
  const displayName = formData.fullName.trim() || '[Full Name & Academic Title/Rank]';
  const displayDept = formData.collegeDept.trim() || '[College/Faculty/Department/Office/Center/etc.]';
  const displayPhone = formData.phoneNumber.trim() || '[Phone Number]';
  const displayEmail = formData.email.trim() || '[Email Address]';

  return (
    <div
      ref={containerRef}
      className="w-full flex justify-center items-start overflow-hidden py-1"
      style={{
        minHeight: `${Math.round(1123 * scaleFactor + 20)}px`,
      }}
    >
      <div
        style={{
          width: '794px',
          transform: `scale(${scaleFactor})`,
          transformOrigin: 'top center',
          marginBottom: `${Math.round(1123 * (scaleFactor - 1))}px`,
        }}
        className="transition-transform duration-200"
      >
        {/* A4 Sheet Container - Use explicit hex styling to avoid Tailwind v4 oklch incompatibility in html2canvas */}
        <div
          id="a4-letter-sheet"
          className="print-container relative font-letter select-text"
          style={{
            width: '794px',
            minHeight: '1123px',
            padding: '76px 72px 80px 72px',
            fontSize: '11.5pt',
            lineHeight: '1.65',
            boxSizing: 'border-box',
            backgroundColor: '#ffffff',
            color: '#111111',
            boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
            border: '1px solid #e2e8f0',
            textAlign: 'left',
          }}
        >
          {/* Optional Letterhead Crest Display */}
          {showLetterheadCrest && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                paddingBottom: '20px',
                marginBottom: '24px',
                borderBottom: '1px solid #d1d5db',
                textAlign: 'center',
              }}
            >
              {customLogoUrl ? (
                <img
                  src={customLogoUrl}
                  alt="Republic Hall Crest"
                  style={{
                    width: '64px',
                    height: '64px',
                    objectFit: 'contain',
                    marginBottom: '8px',
                  }}
                />
              ) : (
                <div style={{ marginBottom: '8px' }}>
                  <RepublicHallCrest size={64} />
                </div>
              )}
              <div
                style={{
                  fontSize: '13pt',
                  fontWeight: 700,
                  color: '#0b6623',
                  letterSpacing: '0.05em',
                  textTransform: 'uppercase',
                }}
              >
                Republic Hall
              </div>
              <div
                style={{
                  fontSize: '9.5pt',
                  letterSpacing: '0.08em',
                  color: '#9a7b1c',
                  fontWeight: 600,
                  textTransform: 'uppercase',
                }}
              >
                Kwame Nkrumah University of Science &amp; Technology, Kumasi
              </div>
              <div
                style={{
                  fontSize: '8.5pt',
                  fontStyle: 'italic',
                  color: '#64748b',
                  marginTop: '2px',
                }}
              >
                Motto: &quot;Set the Pace&quot;
              </div>
            </div>
          )}

          {/* Letter Body strictly following the required formal memo layout */}
          <div style={{ textAlign: 'left', color: '#111111' }}>
            {/* Memo Header Block */}
            <div style={{ paddingBottom: '8px', fontSize: '11.5pt', lineHeight: '1.65' }}>
              <div style={{ display: 'flex' }}>
                <span style={{ width: '80px', fontWeight: 'bold' }}>Date:</span>
                <span style={{ flex: 1 }}>{displayDate}</span>
              </div>
              <div style={{ display: 'flex' }}>
                <span style={{ width: '80px', fontWeight: 'bold' }}>To:</span>
                <span style={{ flex: 1 }}>Hall Warden, Republic Hall</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'flex-start' }}>
                <span style={{ width: '80px', fontWeight: 'bold' }}>From:</span>
                <div style={{ flex: 1 }}>
                  <div>{displayName}</div>
                  <div>{displayDept}, KNUST</div>
                </div>
              </div>
            </div>

            {/* Salutation */}
            <div style={{ paddingTop: '16px', paddingBottom: '4px' }}>
              <span>Dear Hall Master/Warden,</span>
            </div>

            {/* Subject Line (bold and underlined) */}
            <div style={{ paddingTop: '8px', paddingBottom: '8px' }}>
              <span style={{ fontWeight: 'bold', textDecoration: 'underline', letterSpacing: '0.01em' }}>
                APPLICATION FOR FELLOWSHIP OF REPUBLIC HALL, KNUST
              </span>
            </div>

            {/* Formal Letter Content */}
            <div style={{ paddingTop: '8px', textAlign: 'left', lineHeight: '1.65' }}>
              <p style={{ margin: 0 }}>
                I write to formally express my interest in serving as a Fellow of Republic Hall, KNUST. I am eager to actively network and collaborate with other Fellows and past students (alumni) to advance the rich traditions, mentorship networks, and continuous development of the Hall. Furthermore, I am deeply committed to promoting student welfare, academic excellence, and a supportive residential community in close partnership with Hall Management. I thank you for your kind consideration and look forward to hearing favorably from you soon.
              </p>
            </div>

            {/* Sign-off */}
            <div style={{ paddingTop: '28px' }}>
              <div style={{ marginBottom: '8px' }}>Yours faithfully,</div>

              {/* Electronic Signature Image */}
              <div style={{ height: '60px', display: 'flex', alignItems: 'flex-end', marginBottom: '10px' }}>
                {formData.signatureDataUrl ? (
                  <img
                    src={formData.signatureDataUrl}
                    alt="Electronic Signature"
                    style={{
                      maxHeight: '55px',
                      maxWidth: '260px',
                      objectFit: 'contain',
                      display: 'block',
                    }}
                  />
                ) : (
                  <div
                    style={{
                      height: '45px',
                      width: '200px',
                      border: '1px dashed #cbd5e1',
                      borderRadius: '4px',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '10pt',
                      color: '#94a3b8',
                      fontStyle: 'italic',
                    }}
                  >
                    [Signature Required]
                  </div>
                )}
              </div>

              {/* Applicant Name & Details */}
              <div style={{ fontSize: '11.5pt', lineHeight: '1.4' }}>
                <div style={{ fontWeight: 600 }}>{displayName}</div>
                <div>{displayDept}, KNUST</div>
                <div style={{ fontSize: '10.5pt', color: '#334155', marginTop: '2px' }}>
                  Contact: {displayPhone} / {displayEmail}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
