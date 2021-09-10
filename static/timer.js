function countdowntimer(starttime) {
    if(starttime == "no") {
	// countdown not wanted
	return 0;
    }

    var countDownDate = new Date(starttime).getTime();

    // Update the count down every 100 ms
    var x = setInterval(function() {

	// Get today's date and time
	var now = new Date().getTime();

	// Find the distance between now and the count down date
	var distance = countDownDate - now;

	// Time calculations for days, hours, minutes and seconds
	var days = Math.floor(distance / (1000 * 60 * 60 * 24));
	var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
	var seconds = Math.floor((distance % (1000 * 60)) / 1000);

	// Display the result in the element with id="demo"
	var timeuntilstart = "";
	var on = false;
	if(days > 0) {
	    timeuntilstart += days + " days";
	    on = true;
	}
	if(on || hours > 0) {
	    timeuntilstart += " " + hours + " hours";
	    on = true;
	}
	if(on || minutes > 0) {
	    timeuntilstart += " " + minutes + " minutes";
	    on = true;
	}
	if(on || seconds > 0) {
	    timeuntilstart += " " + seconds + " seconds";
	    on = true;
	}

	// If the count down is finished, write some text
	if (on) {
	    document.getElementById("countdown").innerHTML = "Lecture starts in " + timeuntilstart;
	    document.getElementById("countdown").style.color = "red";
	} else {
	    document.getElementById("countdown").innerHTML = "Lecture starts soon";
	    document.getElementById("countdown").style.color = "blue";
	    clearInterval(x);
	}
    }, 100);
}
