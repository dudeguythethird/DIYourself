// The following functions initialise the mobile sidenav component, form select and modal functionality from materialize.

$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('select').formSelect();
    $('.modal').modal();

    // This function reenables some form validation that is precluded by materialise and was provided to me as part of my Code Institute course. 

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        var classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        var classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        // This next line was wrapped in an if statement (" if ($("select.validate").prop("required"))"), however, it didn't seem necessary so I removed it.
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// The following password validation method was found: https://codepen.io/diegoleme/pen/surIK. I have fixed the onchange and onkeyup checks from the original with jQuery and wrapped the code in an if statement that checks which page the user is on. This is to avoid console errors on other pages.
var password = document.getElementById("password"), confirm_password = document.getElementById("password_confirm");
function validatePassword() {
    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}
if (window.location.pathname == '/signup') {
    $("#password").change(validatePassword);
    $("#password_confirm").keyup(validatePassword);
}