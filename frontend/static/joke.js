function addJoke(id_, text) {
    let jokeContainer = document.querySelector("#joke-container");

    let jokeCard = document.createElement('div')
    jokeCard.className = "card border-info mb-4"

    let jokeBody = document.createElement('div')
    jokeBody.className = "card-body m-0"

    let texts = text.split(/\r\n/g)
    for (i = 0; i < texts.length; i++) {
        jokeBody.append(texts[i])
        if (i < texts.length) {
            jokeBody.append(document.createElement('br'))
        }
    }

    jokeCard.appendChild(jokeBody)
    jokeContainer.append(jokeCard)
}

$(document).ready(function () {
    $('#addJokeButton').on('click', function () {
        let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        jQuery.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: "POST",
            url: '/joke/',
            success: function(response) {
                addJoke(response.id_, response.text)
            }
        });
    });
});
