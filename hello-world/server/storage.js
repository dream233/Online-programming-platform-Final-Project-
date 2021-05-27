const STORAGE_KEY = 'chatlist';
export default {
  fetch() {
    return JSON.parse(window.sessionStorage.getItem(STORAGE_KEY) || '[]');
  },
  save(item) {
    window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify(item));
  },
};
