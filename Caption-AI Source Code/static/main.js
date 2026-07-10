// Handles Loader UI and Clipboard copy functionality
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('captionForm');
    const submitBtn = document.getElementById('submitBtn');
    
    if (form) {
        form.addEventListener('submit', function () {
            // Disable button to prevent multi-clicks
            submitBtn.disabled = true;
            submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing Asset Matrix...`;
            
            // Hide output/placeholder and show loading spinner
            if (document.getElementById('placeholderSection')) document.getElementById('placeholderSection').classList.add('d-none');
            if (document.getElementById('outputSection')) document.getElementById('outputSection').classList.add('d-none');
            document.getElementById('loadingSection').classList.remove('d-none');
        });
    }
});

function copyToClipboard() {
    const text = document.getElementById('rawOutputText').innerText;
    navigator.clipboard.writeText(text).then(() => {
        const copyBtn = document.getElementById('copyBtn');
        copyBtn.innerHTML = `✅ Copied Matrix!`;
        copyBtn.className = "btn btn-success btn-sm fw-bold";
        setTimeout(() => {
            copyBtn.innerHTML = `📋 Copy Full Matrix`;
            copyBtn.className = "btn btn-outline-secondary btn-sm fw-bold";
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}