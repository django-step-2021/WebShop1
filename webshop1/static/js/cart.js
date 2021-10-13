$(document).ready(function() {

    $('.add-to-cart-btn').click(function() {
        let productId = $(this).prev().val();

        alert('Select product with ID: ' + productId);
    })

});