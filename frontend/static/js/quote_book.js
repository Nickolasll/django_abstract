function refreshQuotes(quotes) {
    $('[id="quotes"]').slideUp('slow')
    setTimeout(function (){
        for (i = 0; i < quotes.length; i++){
            let picture = document.getElementById('img-' + i);
            let quote = document.getElementById('quote-' + i);
            let profession = document.getElementById('profession-' + i);
            let year = document.createElement('cite');
            picture.src = quotes[i]["picture"];
            year.append(quotes[i]["year"])
            quote.innerText = quotes[i]["quote"];
            profession.innerText = quotes[i]["profession"] + ' ' + quotes[i]["name"] + ', '
            profession.append(year);
        }
        $('[id="quotes"]').slideDown('slow')
    }, 1000);
}

$(document).on('click', '#refresh', function () {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    jQuery.ajax({
        headers: {'X-CSRFToken': csrftoken},
        type: "POST",
        url: '/quote/',
        success: function(response) {
            refreshQuotes(response.quotes)
        },
    });
});