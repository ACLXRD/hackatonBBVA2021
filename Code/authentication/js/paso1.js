let openMic = 0;
function recordAudio() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            $(".loader").css("display", "block");
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            //Storing the audio
            const audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                const audioBlob = new Blob(audioChunks);
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                stream.getTracks()[0].stop();
                saveAudio(audio);
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

function saveAudio(audio) {
    console.log(audio);
}