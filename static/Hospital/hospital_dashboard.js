/* =====================================================
   HemoCampus Hospital Dashboard
   Developed By : Pankaj Upadhyay
===================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Hospital Dashboard Loaded Successfully");

    // ===========================================
    // Counter Animation
    // ===========================================

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = Number(counter.innerText);

        let count = 0;

        const speed = Math.max(1, Math.ceil(target / 60));

        function updateCounter() {

            if (count < target) {

                count += speed;

                if (count > target) {
                    count = target;
                }

                counter.innerText = count;

                requestAnimationFrame(updateCounter);

            } else {

                counter.innerText = target;

            }

        }

        updateCounter();

    });

    // ===========================================
    // Search Filter
    // ===========================================

    const searchInput = document.getElementById("searchInput");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            const filter = this.value.toUpperCase();

            const rows = document.querySelectorAll("#requestTable tbody tr");

            rows.forEach(function (row) {

                const text = row.innerText.toUpperCase();

                row.style.display = text.includes(filter) ? "" : "none";

            });

        });

    }

    // ===========================================
    // Current Date
    // ===========================================

    const dateBox = document.getElementById("currentDate");

    if (dateBox) {

        const today = new Date();

        dateBox.innerHTML = today.toDateString();

    }

    // ===========================================
    // Blood Card Hover Animation
    // ===========================================

    const bloodCards = document.querySelectorAll(".blood-card");

    bloodCards.forEach(function(card){

        card.addEventListener("mouseenter",function(){

            card.style.transform="translateY(-10px)";

        });

        card.addEventListener("mouseleave",function(){

            card.style.transform="translateY(0px)";

        });

    });

    // ===========================================
    // Dashboard Card Animation
    // ===========================================

    const cards=document.querySelectorAll(".dashboard-card");

    cards.forEach(function(card){

        card.addEventListener("mouseenter",function(){

            card.style.transition=".3s";

            card.style.transform="scale(1.03)";

        });

        card.addEventListener("mouseleave",function(){

            card.style.transform="scale(1)";

        });

    });

    // ===========================================
    // Button Ripple Effect
    // ===========================================

    const buttons=document.querySelectorAll(".btn");

    buttons.forEach(function(btn){

        btn.addEventListener("click",function(){

            btn.classList.add("shadow");

            setTimeout(function(){

                btn.classList.remove("shadow");

            },200);

        });

    });

    // ===========================================
    // Loading Spinner
    // ===========================================

    const loader=document.getElementById("loader");

    if(loader){

        window.addEventListener("load",function(){

            loader.style.display="none";

        });

    }

    // ===========================================
    // Table Row Highlight
    // ===========================================

    const rows=document.querySelectorAll("#requestTable tbody tr");

    rows.forEach(function(row){

        row.addEventListener("mouseenter",function(){

            row.style.background="#fff5f5";

        });

        row.addEventListener("mouseleave",function(){

            row.style.background="";

        });

    });

    // ===========================================
    // Notification Click
    // ===========================================

    const notifications=document.querySelectorAll(".list-group-item");

    notifications.forEach(function(item){

        item.addEventListener("click",function(){

            item.style.background="#fee2e2";

            item.style.fontWeight="600";

        });

    });

    // ===========================================
    // Progress Bar Animation
    // ===========================================

    const progressBars=document.querySelectorAll(".progress-bar");

    progressBars.forEach(function(bar){

        const width=bar.style.width;

        bar.style.width="0%";

        setTimeout(function(){

            bar.style.transition="2s";

            bar.style.width=width;

        },300);

    });

});