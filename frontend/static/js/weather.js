$(document).ready(function(){
    $("#add_weather").submit(function(event) {
        event.preventDefault();
        let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let name = $("#city_name").val()
        jQuery.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: "POST",
            url: '/weather/',
            data: JSON.stringify({'city_name': name}),
            success: function(response) {
                console.log(response)
            },
        });
    })
});

