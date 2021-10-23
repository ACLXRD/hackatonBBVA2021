let openMic = 0;
function recordAudio() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            //Storing the audio
            const audioChunks = [];
            mediaRecorder.addEventListener("dataavailable", event => {
                audioChunks.push(event.data);
            });

            mediaRecorder.addEventListener("stop", () => {
                console.log("gola")
                const audioBlob = new Blob(audioChunks);
                const audioUrl = URL.createObjectURL(audioBlob);
                const audio = new Audio(audioUrl);
                stream.getTracks()[0].stop();
                audio.play();
            });
           
            // End audio recording afeter 5 seconds
            setTimeout(() => {
                $("#speaker").prop( "checked", false )
                mediaRecorder.stop();
              }, 5000);
        });
        
}
