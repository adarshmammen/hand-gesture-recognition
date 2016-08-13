var video = document.querySelector("#videoElement");
var canvas = document.querySelector('canvas');
var button = document.querySelector('button');
var ctx = canvas.getContext('2d');
var localMediaStream = null;

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
 
function videoError(e) {
    alert("Could not load video");
}

if (navigator.getUserMedia) {       
    navigator.getUserMedia({video: true}, function(stream) {
    video.src = window.URL.createObjectURL(stream);
    localMediaStream = stream;
  }, videoError);
}
 
function snapshot() {
    if (localMediaStream) {
	ctx.drawImage(video, 0, 0, 680, 480, 0, 0, 500, 375);
	document.querySelector('img').src = canvas.toDataURL('image/png');
	
    }

    $.post('/',
        {
            img : canvas.toDataURL('image/jpeg')
        },
           function(data) {});
}

button.addEventListener('click', snapshot, false);



