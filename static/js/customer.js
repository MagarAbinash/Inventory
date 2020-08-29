$(document).ready(function() {

    $("#purchaseList").on('click', 'button.btn', function (event) {
        let dataId = $(this).data("id");
        $.ajax({
            url: 'purchase_details/' + dataId + '',
            data: {},
            type: 'get',
            success: function(response) {
                $(".details").html(`
                    <div class="List">
                        <h1>This is purchase detials of the single item</h1>
                        <h3>Item: ${ response.item.name }</h3>
                        <h3>Price: ${ response.item.price }</h3>
                        <h3>Quantity: ${ response.list.quantity }</h3>
                        <h3>Date: ${ response.list.date }</h3>
                    </div>
                `)
            }
        })
    });

});