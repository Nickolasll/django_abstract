function addJoke(id_, text) {
    let jokeContainer = document.querySelector("#joke-container");

    let jokeCard = document.createElement('div');

    jokeCard.className = "card border-info mb-4 hide";
    jokeCard.setAttribute('joke-id', id_);

    let closeButton = document.createElement('button');
    closeButton.className = "close";
    closeButton.type = "button";
    closeButton.setAttribute('aria-label', 'Close')
    closeButton.style = "box-shadow: none !important; outline: 0px !important;";
    let buttonSpan = document.createElement('span');
    buttonSpan.setAttribute('aria-hidden', "true");
    buttonSpan.innerHTML = '&times;';
    closeButton.appendChild(buttonSpan);

    let jokeBody = document.createElement('div')
    jokeBody.className = "card-body m-0"
    jokeBody.append(closeButton)

    let texts = text.split(/\r\n/g)
    for (i = 0; i < texts.length; i++) {
        jokeBody.append(texts[i])
        if (i < texts.length) {
            jokeBody.append(document.createElement('br'))
        }
    }

    jokeCard.appendChild(jokeBody);
    jokeContainer.append(jokeCard);
    $('[joke-id="'+id_+'"]').hide()
    $('[joke-id="'+id_+'"]').slideDown('slow')
}

$(document).on('click', '#addJokeButton', function () {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    jQuery.ajax({
        headers: {'X-CSRFToken': csrftoken},
        type: "POST",
        url: '/joke/',
        success: function(response) {
            addJoke(response.id_, response.text)
        },
    });
});

$(document).on('click', 'button.close',function(){
    let  id_ = $(this).closest('[joke-id]').attr('joke-id');
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    jQuery.ajax({
        headers: {'X-CSRFToken': csrftoken},
        type: "DELETE",
        url: '/joke/',
        data: JSON.stringify({"id_": id_}),
        contentType:'application/json',
        dataType: 'text',
        success: function(response) {
            $("[joke-id="+id_+"]").clsssName = "card border-info";
            $("[joke-id="+id_+"]").slideUp('slow')
            setTimeout(function (){
                document.querySelector('[joke-id="'+id_+'"]').remove()
            }, 1000);
        },
    });
});
