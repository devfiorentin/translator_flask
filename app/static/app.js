const copyToClipboard = async (str) => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
        return await navigator.clipboard.writeText(str);
    }
 
};

const copyResultadoToClipboard = () => {
    const resultadoElement = document.getElementById('resultado');
    const resultadoText = resultadoElement.innerText;

    copyToClipboard(resultadoText).then(() => {

    }).catch((error) => {
        console.error('Erro ao copiar para a área de transferência: ', error);
    });
};