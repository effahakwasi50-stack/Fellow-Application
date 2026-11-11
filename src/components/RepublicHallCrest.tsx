import React from 'react';

interface CrestProps {
  className?: string;
  size?: number;
}

/**
 * Republic Hall KNUST Official Circular Crest SVG
 * "REPUBLIC HALL, KWAME NKRUMAH UNIV. OF SCIENCE & TECH., KUMASI - SET THE PACE"
 */
export const RepublicHallCrest: React.FC<CrestProps> = ({ className = '', size = 56 }) => {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 200 200"
      className={`shrink-0 ${className}`}
      aria-label="Republic Hall KNUST Crest - Set The Pace"
      role="img"
    >
      <defs>
        {/* Outer green gradient */}
        <linearGradient id="hallGreenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0b6623" />
          <stop offset="100%" stopColor="#074417" />
        </linearGradient>

        {/* Gold gradient */}
        <linearGradient id="hallGoldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#f7e07c" />
          <stop offset="40%" stopColor="#d4af37" />
          <stop offset="100%" stopColor="#9a7b1c" />
        </linearGradient>

        {/* Curved path for top text */}
        <path
          id="textPathTop"
          d="M 28 100 A 72 72 0 1 1 172 100"
          fill="none"
        />

        {/* Curved path for bottom text */}
        <path
          id="textPathBottom"
          d="M 172 100 A 72 72 0 0 1 28 100"
          fill="none"
        />
      </defs>

      {/* Outer rim gold border */}
      <circle cx="100" cy="100" r="98" fill="url(#hallGoldGrad)" stroke="#785e13" strokeWidth="1.5" />
      
      {/* Outer ring deep green */}
      <circle cx="100" cy="100" r="92" fill="url(#hallGreenGrad)" stroke="url(#hallGoldGrad)" strokeWidth="2" />
      
      {/* Inner ring gold border */}
      <circle cx="100" cy="100" r="66" fill="#fcfbf7" stroke="url(#hallGoldGrad)" strokeWidth="3" />

      {/* Top curved text */}
      <text fill="#ffffff" fontSize="13" fontWeight="800" letterSpacing="2.5" fontFamily="system-ui, sans-serif">
        <textPath href="#textPathTop" startOffset="50%" textAnchor="middle">
          REPUBLIC HALL
        </textPath>
      </text>

      {/* Bottom curved text */}
      <text fill="#ffffff" fontSize="7.8" fontWeight="700" letterSpacing="0.8" fontFamily="system-ui, sans-serif">
        <textPath href="#textPathBottom" startOffset="50%" textAnchor="middle">
          KWAME NKRUMAH UNIV. OF SCI. &amp; TECH.
        </textPath>
      </text>

      {/* Small gold stars separating top and bottom text */}
      <g fill="#d4af37">
        <polygon points="24,100 26,103 29,103 27,105 28,108 24,106 20,108 21,105 19,103 22,103" />
        <polygon points="176,100 178,103 181,103 179,105 180,108 176,106 172,108 173,105 171,103 174,103" />
      </g>

      {/* Central Emblem: Eagle / Shield / Torch of Knowledge & Traditional Akan Stool / Adinkra Gye Nyame motif */}
      {/* Shield Background */}
      <path
        d="M 68 62 L 132 62 C 132 94 122 114 100 128 C 78 114 68 94 68 62 Z"
        fill="#0b6623"
        stroke="url(#hallGoldGrad)"
        strokeWidth="2.5"
      />

      {/* Shield split / Gold diagonal stripe */}
      <path
        d="M 70 64 L 95 64 L 128 100 C 122 110 112 118 100 125 L 70 88 Z"
        fill="#d4af37"
        opacity="0.25"
      />

      {/* Torch of Enlightenment */}
      <g transform="translate(100, 72) scale(0.65)">
        {/* Flame */}
        <path
          d="M 0 -22 C -6 -12 -8 -4 0 4 C 8 -4 6 -12 0 -22 Z"
          fill="#e65100"
        />
        <path
          d="M 0 -18 C -3 -11 -4 -5 0 1 C 4 -5 3 -11 0 -18 Z"
          fill="#ffb300"
        />
        {/* Torch Bowl */}
        <path
          d="M -12 4 L 12 4 L 6 16 L -6 16 Z"
          fill="url(#hallGoldGrad)"
          stroke="#785e13"
          strokeWidth="1"
        />
        {/* Torch Handle */}
        <path
          d="M -4 16 L 4 16 L 2 34 L -2 34 Z"
          fill="url(#hallGoldGrad)"
        />
      </g>

      {/* Open Book of Academic Excellence */}
      <g transform="translate(100, 106) scale(0.68)">
        <path
          d="M 0 -2 C -12 -10 -28 -8 -32 -2 L -32 16 C -28 10 -12 8 0 16 C 12 8 28 10 32 16 L 32 -2 C 28 -8 12 -10 0 -2 Z"
          fill="#ffffff"
          stroke="#0b6623"
          strokeWidth="1.5"
        />
        {/* Spine */}
        <line x1="0" y1="-2" x2="0" y2="16" stroke="#0b6623" strokeWidth="2" />
        {/* Book lines */}
        <line x1="-24" y1="2" x2="-6" y2="-1" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
        <line x1="-24" y1="6" x2="-6" y2="3" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
        <line x1="-24" y1="10" x2="-6" y2="7" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
        <line x1="6" y1="-1" x2="24" y2="2" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
        <line x1="6" y1="3" x2="24" y2="6" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
        <line x1="6" y1="7" x2="24" y2="10" stroke="#0b6623" strokeWidth="1" opacity="0.6" />
      </g>

      {/* Motto Banner at Base: "SET THE PACE" */}
      <g transform="translate(100, 150)">
        {/* Ribbon banner background */}
        <path
          d="M -68 0 L -60 -10 L -46 -5 L 46 -5 L 60 -10 L 68 0 L 56 12 L -56 12 Z"
          fill="#d4af37"
          stroke="#785e13"
          strokeWidth="1.2"
        />
        {/* Ribbon folds */}
        <polygon points="-56,12 -46,-5 -46,12" fill="#9a7b1c" />
        <polygon points="56,12 46,-5 46,12" fill="#9a7b1c" />
        {/* Ribbon text */}
        <text
          x="0"
          y="7"
          fill="#084c1a"
          fontSize="9.5"
          fontWeight="900"
          letterSpacing="1.8"
          textAnchor="middle"
          fontFamily="system-ui, sans-serif"
        >
          SET THE PACE
        </text>
      </g>
    </svg>
  );
};
