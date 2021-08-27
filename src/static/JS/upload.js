const dropArea = document.querySelector("#dropContainer");
let file;
let input = document.querySelector("#file");

dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add('active');
})
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove('active');
})
dropArea.addEventListener("drop", (event) => {
    console.log(input.value)
    event.preventDefault();
    file = event.dataTransfer.files[0];
    let fileType = file.type;
    let valid = ["image/jpeg", "image/png", "image/jpeg"];
    if (valid.includes(fileType)) {
        console.log(1);
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;
            fileURL = dataURLtoFile(fileURL, file);
            console.log(fileURL)
            input.value = fileURL;

            console.log(input.value)
        }
        fileReader.readAsDataURL(file);
    } else {
        console.log(0);
        dropArea.classList.remove('active');
    }
})

function dataURLtoFile(dataurl, filename) {

    var arr = dataurl.split(','),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);

    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], filename, { type: mime });
}