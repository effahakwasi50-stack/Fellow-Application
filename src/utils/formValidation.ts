/**
 * Form validation and formatting utilities for Republic Hall Fellow Application
 */

export interface FellowFormData {
  fullName: string;
  collegeDept: string;
  phoneNumber: string;
  email: string;
  applicationDate: string;
  signatureDataUrl: string;
}

export interface ValidationResult {
  isValid: boolean;
  errors: Partial<Record<keyof FellowFormData, string>>;
  missingFields: string[];
}

export function formatApplicationDate(dateInput?: Date | string): string {
  const date = dateInput ? new Date(dateInput) : new Date();
  if (isNaN(date.getTime())) {
    return '';
  }
  return date.toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric',
  });
}

export function sanitizeFileName(name: string): string {
  const cleanName = (name || 'Applicant')
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '_');
  return `Republic_Hall_Fellow_Application_${cleanName || 'Applicant'}.pdf`;
}

export function validateApplication(data: FellowFormData): ValidationResult {
  const errors: Partial<Record<keyof FellowFormData, string>> = {};
  const missingFields: string[] = [];

  const trimmedName = (data.fullName || '').trim();
  if (!trimmedName) {
    errors.fullName = 'Full Name & Academic Title/Rank is required.';
    missingFields.push('Full Name & Academic Title/Rank');
  }

  const trimmedDept = (data.collegeDept || '').trim();
  if (!trimmedDept) {
    errors.collegeDept = 'College / Department / Office is required.';
    missingFields.push('College / Department / Office');
  }

  const trimmedPhone = (data.phoneNumber || '').trim();
  if (!trimmedPhone) {
    errors.phoneNumber = 'Phone Number is required.';
    missingFields.push('Phone Number');
  } else if (!/^[0-9+\s\-()]{7,20}$/.test(trimmedPhone)) {
    errors.phoneNumber = 'Please enter a valid phone number (e.g. 0240000000).';
    missingFields.push('Valid Phone Number');
  }

  const trimmedEmail = (data.email || '').trim();
  if (!trimmedEmail) {
    errors.email = 'Email Address is required.';
    missingFields.push('Email Address');
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(trimmedEmail)) {
    errors.email = 'Please enter a valid email address.';
    missingFields.push('Valid Email Address');
  }

  const trimmedDate = (data.applicationDate || '').trim();
  if (!trimmedDate) {
    errors.applicationDate = 'Application Date is required.';
    missingFields.push('Application Date');
  }

  const trimmedSignature = (data.signatureDataUrl || '').trim();
  if (!trimmedSignature) {
    errors.signatureDataUrl = 'Electronic signature is required.';
    missingFields.push('Electronic Signature');
  }

  return {
    isValid: missingFields.length === 0,
    errors,
    missingFields,
  };
}

/**
 * Creates a clean default vector signature data URL for initial sample display
 */
export function createSampleSignatureSvg(): string {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 70" width="280" height="70">
    <path d="M 20 45 Q 45 15, 75 35 T 120 40 Q 140 10, 165 42 T 210 38 Q 235 25, 260 48" fill="none" stroke="#000080" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M 60 48 Q 110 54, 240 45" fill="none" stroke="#000080" stroke-width="1.8" stroke-linecap="round"/>
    <circle cx="122" cy="22" r="2.5" fill="#000080" />
  </svg>`;
  return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
}

export function getDefaultFormData(): FellowFormData {
  return {
    fullName: 'Dr. John Mensah, Senior Lecturer',
    collegeDept: 'College of Engineering / Dept. of Mechanical Engineering',
    phoneNumber: '0240000000',
    email: 'jmensah@knust.edu.gh',
    applicationDate: formatApplicationDate(),
    signatureDataUrl: createSampleSignatureSvg(),
  };
}
