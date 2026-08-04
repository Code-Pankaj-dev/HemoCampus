/*====================================================
        HEMOCAMPUS DONOR DASHBOARD
        JavaScript
=====================================================*/

document.addEventListener("DOMContentLoaded", function () {

    console.log("HemoCampus Donor Dashboard Loaded");

    startCounters();

    updateDateTime();

    setInterval(updateDateTime, 1000);

    enableTooltips();

    animateProgressBars();

    initializeSearch();

    initializeSpinner();

});


/*====================================================
        COUNTER ANIMATION
=====================================================*/

function startCounters() {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.innerText);

        let count = 0;

        const speed = Math.max(10, Math.floor(target / 80));

        const timer = setInterval(() => {

            count += speed;

            if (count >= target) {

                counter.innerText = target;

                clearInterval(timer);

            } else {

                counter.innerText = count;

            }

        }, 20);

    });

}


/*====================================================
        DATE & TIME
=====================================================*/

function updateDateTime() {

    const box = document.getElementById("currentDateTime");

    if (!box) return;

    const now = new Date();

    box.innerHTML = now.toLocaleString();

}


/*====================================================
        SEARCH
=====================================================*/

function initializeSearch() {

    const input = document.getElementById("tableSearch");

    if (!input) return;

    input.addEventListener("keyup", function () {

        const value = this.value.toLowerCase();

        const rows = document.querySelectorAll("tbody tr");

        rows.forEach(row => {

            row.style.display = row.innerText.toLowerCase().includes(value)

                ? ""

                : "none";

        });

    });

}


/*====================================================
        LOADING SPINNER
=====================================================*/

function initializeSpinner() {

    const spinner = document.getElementById("loader");

    if (!spinner) return;

    spinner.style.display = "flex";

    window.addEventListener("load", function () {

        spinner.style.display = "none";

    });

}


/*====================================================
        PROGRESS BAR
=====================================================*/

function animateProgressBars() {

    const bars = document.querySelectorAll(".progress-bar");

    bars.forEach(bar => {

        const width = bar.style.width;

        bar.style.width = "0%";

        setTimeout(() => {

            bar.style.width = width;

        }, 300);

    });

}


/*====================================================
        TOOLTIP
=====================================================*/

function enableTooltips() {

    const tooltipTriggerList = [].slice.call(

        document.querySelectorAll('[data-bs-toggle="tooltip"]')

    );

    tooltipTriggerList.map(function (tooltipTriggerEl) {

        return new bootstrap.Tooltip(tooltipTriggerEl);

    });

}


/*====================================================
        CARD HOVER EFFECT
=====================================================*/

document.querySelectorAll(".dashboard-card").forEach(card => {

    card.addEventListener("mouseenter", function () {

        this.style.transform = "translateY(-8px)";

    });

    card.addEventListener("mouseleave", function () {

        this.style.transform = "translateY(0px)";

    });

});


/*====================================================
        NOTIFICATION
=====================================================*/

function showNotification(message) {

    const notification = document.createElement("div");

    notification.className = "alert alert-success position-fixed";

    notification.style.top = "20px";

    notification.style.right = "20px";

    notification.style.zIndex = "9999";

    notification.innerHTML = message;

    document.body.appendChild(notification);

    setTimeout(() => {

        notification.remove();

    }, 3000);

}


/*====================================================
        SMOOTH SCROLL
=====================================================*/

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});


/*====================================================
        PAGE LOADER
=====================================================*/

window.onload = function () {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.style.display = "none";

    }

};


/*====================================================
        CONSOLE MESSAGE
=====================================================*/

console.log("HemoCampus Donor Dashboard Ready");