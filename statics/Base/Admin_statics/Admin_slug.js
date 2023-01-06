function string_to_slug(str) {
    str = str.replace(/^\s+|\s+$/g, ''); // trim
    str = str.toLowerCase();

    // remove accents, swap ñ for n, etc
    var from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;";
    var to = "aaaaeeeeiiiioooouuuunc------";
    for (var i = 0, l = from.length; i < l; i++) {
        str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
    }

    str = str.replace(/[^a-z0-9 -]/g, '') // remove invalid chars
        .replace(/\s+/g, '-') // collapse whitespace and replace by -
        .replace(/-+/g, '-'); // collapse dashes

    return str;
}



window.onload = function () {
    var input_var = document.querySelectorAll('div.form-row.field-name>div>input')[0];
    var output_var = document.querySelectorAll('div.form-row.field-slug>div>div.readonly')[0];
    var output_add = document.querySelector("#id_slug")
    var extra_fieldsets = document.querySelectorAll("div > fieldset.collapse")
    for (let i = 0; i < extra_fieldsets.length; i++) {
        let text_area = extra_fieldsets[i].querySelectorAll("textarea.vLargeTextField")
        if (text_area) {
            for (let j = 0; j < text_area.length; j++) {
                text_area[j].setAttribute('class','vTextField')
                text_area[j].setAttribute('cols','1')
                text_area[j].setAttribute('rows','1')
            }
        }
    }

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
