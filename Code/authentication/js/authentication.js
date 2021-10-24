let openMic = 0;
function recordAudio() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            $(".loader").css("display", "block");
            $('#change').css("display", "none");
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            //Storing the audio
            const audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks, {type:'audio/webm'});
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                stream.getTracks()[0].stop();
                saveAudio(audioBlob);
                $('#microphone').css("display", "none");
                $('#btnSiguiente').css("display", "inline-block");
                audio.play();
            });
           
            // End audio recording afeter 5 seconds
            setTimeout(() => {
                $("#speaker").prop( "checked", false )
                mediaRecorder.stop();
                $(".loader").css("display", "none");
              }, 5000);
        });
}

function saveAudio(file) {
    const formData = new FormData();
    formData.append('audio-file', file);
    return fetch('http://localhost:5000/audio', {
        method: 'POST',
        body: formData,
        headers:{
            fileName:'audio.mp3'
        }
    });
}