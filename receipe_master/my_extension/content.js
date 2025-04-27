chrome.storage.local.get(['highlightText'], (result) => {
    if (result.highlightText) {
        const text = result.highlightText;
        const bodyText = document.body.innerHTML;
        const highlighted = bodyText.replace(new RegExp(text, 'gi'), `<mark>${text}</mark>`);
        document.body.innerHTML = highlighted;
    }
});
