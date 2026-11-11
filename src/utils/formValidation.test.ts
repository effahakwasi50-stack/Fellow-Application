import test from 'node:test';
import assert from 'node:assert/strict';
import {
  formatApplicationDate,
  sanitizeFileName,
  validateApplication,
  getDefaultFormData,
  FellowFormData,
} from './formValidation.ts';

test('formatApplicationDate formats date correctly', () => {
  const formatted = formatApplicationDate('2026-11-11');
  assert.match(formatted, /November 11, 2026/);
});

test('sanitizeFileName produces expected pdf file name', () => {
  assert.equal(
    sanitizeFileName('Dr. John Mensah'),
    'Republic_Hall_Fellow_Application_Dr_John_Mensah.pdf'
  );
  assert.equal(
    sanitizeFileName('Prof. Kwaku Osei-Tutu'),
    'Republic_Hall_Fellow_Application_Prof_Kwaku_Osei-Tutu.pdf'
  );
  assert.equal(
    sanitizeFileName(''),
    'Republic_Hall_Fellow_Application_Applicant.pdf'
  );
});

test('validateApplication accepts valid sample data', () => {
  const data = getDefaultFormData();
  const result = validateApplication(data);
  assert.equal(result.isValid, true);
  assert.equal(result.missingFields.length, 0);
});

test('validateApplication catches empty required fields', () => {
  const invalidData: FellowFormData = {
    fullName: '',
    collegeDept: '',
    phoneNumber: '',
    email: '',
    applicationDate: '',
    signatureDataUrl: '',
  };
  const result = validateApplication(invalidData);
  assert.equal(result.isValid, false);
  assert.equal(result.missingFields.length, 6);
  assert.ok(result.errors.fullName);
  assert.ok(result.errors.collegeDept);
  assert.ok(result.errors.phoneNumber);
  assert.ok(result.errors.email);
  assert.ok(result.errors.applicationDate);
  assert.ok(result.errors.signatureDataUrl);
});

test('validateApplication catches invalid email and phone formats', () => {
  const data: FellowFormData = {
    fullName: 'Jane Doe',
    collegeDept: 'Faculty of Law',
    phoneNumber: 'abc-invalid',
    email: 'notanemail',
    applicationDate: 'November 11, 2026',
    signatureDataUrl: 'data:image/png;base64,sample',
  };
  const result = validateApplication(data);
  assert.equal(result.isValid, false);
  assert.ok(result.errors.phoneNumber);
  assert.ok(result.errors.email);
});
