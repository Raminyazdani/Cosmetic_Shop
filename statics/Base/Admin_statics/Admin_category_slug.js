

function get_slug(str) {
   const re_slice = /Slug :.*/g;
   var new_string = re_slice.exec(str);
    return new_string[0].slice(6)
}
window.onload = function () {
    var input_var = document.querySelectorAll('div.form-row.field-name>div>input')[0];
    var output_var = document.querySelectorAll('div.form-row.field-slug>div>div.readonly')[0];
    var output_add = document.querySelector("#id_slug")

    var parent_var_select = document.querySelector("#id_parent")
    console.log(parent_var_select)

    var extra_fieldsets = document.querySelectorAll("div > fieldset.collapse")
    for (let i = 0; i < extra_fieldsets.length; i++) {
        let text_area = extra_fieldsets[i].querySelectorAll("textarea.vLargeTextField")
        if (text_area) {
            for (let j = 0; j < text_area.length; j++) {
                text_area[j].setAttribute('class', 'vTextField')
                text_area[j].setAttribute('cols', '1')
                text_area[j].setAttribute('rows', '1')
            }
        }
    }

    if (input_var && output_var) {
        input_var.addEventListener("input", function () {
            parent_var = $("#id_parent option:selected")
            if (parent_var.text() == "---------") {
                output_var.innerHTML = string_to_slug(this.value);
            }
            else {
                output_var.innerHTML = get_slug(parent_var.text()) + "/" + string_to_slug(this.value);

            }
        })
        parent_var_select.addEventListener("change", function () {
            parent_var = $("#id_parent option:selected")
            if (parent_var.text() == "---------") {
                output_var.innerHTML = string_to_slug(input_var.value);
            } else {
                output_var.innerHTML = get_slug(parent_var.text()) + "/" + string_to_slug(input_var.value);
            }
        })

    }
    if (input_var && output_add) {
        output_add.setAttribute("readonly", "readonly");
        input_var.addEventListener("input", function () {
            output_add.innerHTML = string_to_slug(this.value);
        })
    }
}
