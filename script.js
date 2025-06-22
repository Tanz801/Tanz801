const inputText = document.getElementById('input');
const outputText = document.getElementById('output');
const lang = document.getElementById('options');

let debounceTimeout = null;
let latestInput = '';
let controller = null;

function debounceTrans() {
    clearTimeout(debounceTimeout);
    if (inputText.value.trim().length != 0) {
    outputText.value = "Translating...";
    debounceTimeout = setTimeout(() => {
        latestInput = inputText.value;
        checkTrans();
        
    }, 800);
    }

};

function checkTrans() {
    if (controller) {
        controller.abort()
    }; 

    outputText.value = "Translating...";
    
    controller = new AbortController();
    const signal = controller.signal;

    const input = latestInput;
    const selectedLang = lang.value;

    fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            input: input,
            options: selectedLang
        }),
        signal: signal
    })
    .then(response => response.json())
    .then(data => {

        if (input === inputText.value) {
            outputText.value = data.translated;
        }
    })
    .catch(err => console.error('Error:', err))
}


inputText.addEventListener('input', debounceTrans);
lang.addEventListener('change', debounceTrans);

