import React from 'react';
import {
  FellowFormData,
  getDefaultFormData,
  formatApplicationDate,
} from '../utils/formValidation.ts';
import { SignaturePad } from './SignaturePad.tsx';
import {
  User,
  Building2,
  Phone,
  Mail,
  Calendar,
  RotateCcw,
  Eraser,
  HelpCircle,
  AlertTriangle,
} from 'lucide-react';

interface ApplicationFormProps {
  formData: FellowFormData;
  onChange: (updated: Partial<FellowFormData>) => void;
  errors: Partial<Record<keyof FellowFormData, string>>;
  onResetSample: () => void;
  onClearAll: () => void;
}

export const ApplicationForm: React.FC<ApplicationFormProps> = ({
  formData,
  onChange,
  errors,
  onResetSample,
  onClearAll,
}) => {
  // Quick today setter for date
  const setTodayDate = () => {
    onChange({ applicationDate: formatApplicationDate(new Date()) });
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200/90 p-5 sm:p-6 space-y-6">
      {/* Header of Form */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-100">
        <div>
          <h2 className="text-lg font-bold text-[#0b6623] flex items-center gap-2">
            <span>Applicant Information</span>
            <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-amber-50 text-amber-800 border border-amber-200">
              Compulsory Fields (*)
            </span>
          </h2>
          <p className="text-xs text-slate-500 mt-0.5">
            Complete all details and provide your electronic signature to generate the official letter.
          </p>
        </div>

        {/* Quick action buttons */}
        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={onResetSample}
            className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold text-emerald-800 bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 transition-colors"
            title="Load standard sample data"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            Sample Data
          </button>
          <button
            type="button"
            onClick={onClearAll}
            className="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-600 bg-slate-100 hover:bg-slate-200 border border-slate-200 transition-colors"
            title="Clear all inputs"
          >
            <Eraser className="w-3.5 h-3.5" />
            Clear
          </button>
        </div>
      </div>

      {/* Inputs Form */}
      <div className="space-y-4">
        {/* Full Name & Academic Title/Rank */}
        <div>
          <label
            htmlFor="fullName"
            className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1"
          >
            Full Name &amp; Academic Title/Rank <span className="text-red-600 font-bold">*</span>
          </label>
          <div className="relative rounded-lg shadow-sm">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
              <User className="h-4 w-4" />
            </div>
            <input
              type="text"
              id="fullName"
              name="fullName"
              value={formData.fullName}
              onChange={(e) => onChange({ fullName: e.target.value })}
              placeholder="e.g. Dr. John Mensah, Senior Lecturer"
              className={`block w-full pl-9 pr-3 py-2 text-sm rounded-lg border transition-colors ${
                errors.fullName
                  ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500 bg-red-50/20'
                  : 'border-slate-300 focus:border-[#0b6623] focus:ring-1 focus:ring-[#0b6623] bg-white'
              }`}
              required
            />
          </div>
          {errors.fullName ? (
            <p className="mt-1 text-xs text-red-600 font-medium">{errors.fullName}</p>
          ) : (
            <p className="mt-1 text-[11px] text-slate-400">
              Include honorary title, prefix (e.g., Prof., Dr., Mr., Mrs.), and university rank.
            </p>
          )}
        </div>

        {/* College / Department */}
        <div>
          <label
            htmlFor="collegeDept"
            className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1"
          >
            College / Faculty / Department / Office / Center <span className="text-red-600 font-bold">*</span>
          </label>
          <div className="relative rounded-lg shadow-sm">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
              <Building2 className="h-4 w-4" />
            </div>
            <input
              type="text"
              id="collegeDept"
              name="collegeDept"
              value={formData.collegeDept}
              onChange={(e) => onChange({ collegeDept: e.target.value })}
              placeholder="e.g. College of Engineering / Dept. of Mechanical Engineering"
              className={`block w-full pl-9 pr-3 py-2 text-sm rounded-lg border transition-colors ${
                errors.collegeDept
                  ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500 bg-red-50/20'
                  : 'border-slate-300 focus:border-[#0b6623] focus:ring-1 focus:ring-[#0b6623] bg-white'
              }`}
              required
            />
          </div>
          {errors.collegeDept ? (
            <p className="mt-1 text-xs text-red-600 font-medium">{errors.collegeDept}</p>
          ) : (
            <p className="mt-1 text-[11px] text-slate-400">
              State your primary academic college, faculty, institute, or university unit.
            </p>
          )}
        </div>

        {/* Two Columns: Phone Number & Email Address */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {/* Phone Number */}
          <div>
            <label
              htmlFor="phoneNumber"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1"
            >
              Phone Number <span className="text-red-600 font-bold">*</span>
            </label>
            <div className="relative rounded-lg shadow-sm">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                <Phone className="h-4 w-4" />
              </div>
              <input
                type="tel"
                id="phoneNumber"
                name="phoneNumber"
                value={formData.phoneNumber}
                onChange={(e) => onChange({ phoneNumber: e.target.value })}
                placeholder="0240000000"
                className={`block w-full pl-9 pr-3 py-2 text-sm rounded-lg border transition-colors ${
                  errors.phoneNumber
                    ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500 bg-red-50/20'
                    : 'border-slate-300 focus:border-[#0b6623] focus:ring-1 focus:ring-[#0b6623] bg-white'
                }`}
                required
              />
            </div>
            {errors.phoneNumber && (
              <p className="mt-1 text-xs text-red-600 font-medium">{errors.phoneNumber}</p>
            )}
          </div>

          {/* Email Address */}
          <div>
            <label
              htmlFor="email"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-1"
            >
              Email Address <span className="text-red-600 font-bold">*</span>
            </label>
            <div className="relative rounded-lg shadow-sm">
              <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
                <Mail className="h-4 w-4" />
              </div>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={(e) => onChange({ email: e.target.value })}
                placeholder="jmensah@knust.edu.gh"
                className={`block w-full pl-9 pr-3 py-2 text-sm rounded-lg border transition-colors ${
                  errors.email
                    ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500 bg-red-50/20'
                    : 'border-slate-300 focus:border-[#0b6623] focus:ring-1 focus:ring-[#0b6623] bg-white'
                }`}
                required
              />
            </div>
            {errors.email && (
              <p className="mt-1 text-xs text-red-600 font-medium">{errors.email}</p>
            )}
          </div>
        </div>

        {/* Application Date */}
        <div>
          <div className="flex items-center justify-between mb-1">
            <label
              htmlFor="applicationDate"
              className="block text-xs font-bold uppercase tracking-wider text-slate-700"
            >
              Application Date <span className="text-red-600 font-bold">*</span>
            </label>
            <button
              type="button"
              onClick={setTodayDate}
              className="text-[11px] font-semibold text-[#0b6623] hover:underline"
            >
              Set Today's Date
            </button>
          </div>
          <div className="relative rounded-lg shadow-sm">
            <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400">
              <Calendar className="h-4 w-4" />
            </div>
            <input
              type="text"
              id="applicationDate"
              name="applicationDate"
              value={formData.applicationDate}
              onChange={(e) => onChange({ applicationDate: e.target.value })}
              placeholder="e.g. November 11, 2026"
              className={`block w-full pl-9 pr-3 py-2 text-sm rounded-lg border transition-colors ${
                errors.applicationDate
                  ? 'border-red-400 focus:border-red-500 focus:ring-1 focus:ring-red-500 bg-red-50/20'
                  : 'border-slate-300 focus:border-[#0b6623] focus:ring-1 focus:ring-[#0b6623] bg-white'
              }`}
              required
            />
          </div>
          {errors.applicationDate ? (
            <p className="mt-1 text-xs text-red-600 font-medium">{errors.applicationDate}</p>
          ) : (
            <p className="mt-1 text-[11px] text-slate-400">
              Standard format: Month DD, YYYY (e.g. {formatApplicationDate(new Date())})
            </p>
          )}
        </div>

        {/* Electronic Signature Section */}
        <div className="pt-2">
          <SignaturePad
            signature={formData.signatureDataUrl}
            onChange={(sig) => onChange({ signatureDataUrl: sig })}
            error={errors.signatureDataUrl}
          />
        </div>
      </div>

      {/* Helpful Guidelines Callout */}
      <div className="p-3.5 bg-slate-50 rounded-lg border border-slate-200/80 text-xs text-slate-600 space-y-1.5">
        <div className="flex items-center gap-1.5 font-bold text-slate-800 text-xs">
          <HelpCircle className="w-4 h-4 text-[#0b6623]" />
          <span>Note for Senior Members / Prospective Fellows</span>
        </div>
        <p className="text-slate-600 leading-relaxed text-[11.5px]">
          Fellowship of Republic Hall is open to Senior Members of KNUST dedicated to fostering student mentorship, residential hall governance, and alumni engagement. The completed application letter will be formally delivered to the Hall Warden, Republic Hall.
        </p>
      </div>
    </div>
  );
};
