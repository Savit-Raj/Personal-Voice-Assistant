$(document).ready(function () {

    // text animation
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn"
        },
        out: {
            effect: "bounceOut"
        },
    });

    // siri ios9
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeOutUp",
            sync: true
        },
    });

    // mic button click event
    $("#MicBtn").click(function () {
        eel.playAssistantSound()
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });

    function doc_keyUp(e) {
        if (e.key === 'v') {
            eel.playAssistantSound()
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);
});