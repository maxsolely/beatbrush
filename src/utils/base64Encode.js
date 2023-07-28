/**
 * Encodes the binary data provided
 * @param {Blob} blob Binary data to encode - https://developer.mozilla.org/en-US/docs/Web/API/Blob
 * @returns {Promise<string>} A base64 encoded string
 */
export default async function base64Encode(blob) {
 return new Promise((resolve) => {
  const reader = new FileReader();
  reader.onloadend = () => resolve(reader.result.split('base64,')[1]);
  reader.readAsDataURL(blob);
 });
}
