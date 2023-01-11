

window.onload = function () {
    var input_var = document.querySelectorAll('div.form-row.field-phone_number>div>input')[0];
    var output_var = document.querySelectorAll('div.form-row.field-slug>div>div.readonly')[0];
    var output_add = document.querySelector("#id_slug")
    console.log(input_var)
    if (input_var && output_var) {
        input_var.addEventListener("input", function () {
            output_var.innerHTML = string_to_slug(this.value);
        })
    }
    if (input_var && output_add) {
        output_add.setAttribute("readonly", "readonly");
        input_var.addEventListener("input", function () {
            output_add.innerHTML = string_to_slug(this.value);
        })
    }
}