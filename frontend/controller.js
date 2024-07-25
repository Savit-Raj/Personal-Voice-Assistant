
$(document).ready(function () {
    // Display Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }

    // Display Hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#oval").attr("hidden", false)
        $("#SiriWave").attr("hidden", true)
    }

    // Toggle visibility when speech recognition fails
    eel.expose(ToggleVisibility)
    function ToggleVisibility() {
        $("#oval").attr("hidden", false)
        $("#SiriWave").attr("hidden", true)
    }
});



