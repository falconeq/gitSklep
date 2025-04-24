var updateBtns = document.getElementsByClassName('update-cart');

for (i=0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("productId:", productId, "action:", action);
        console.log('User:', user);

        if (user == 'AnonymousUser'){
            console.log("User is not authenticated...")
        } else{
            console.log("User is authenticated:", user)
            // wywołać metode dodawania do koszyka
        }
    });
}

function updateUserOrder(productId, action){
    var url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    }).then((response) => {
        return response.json();
    }).then((data) => {
        console.log('Data:', data);
    });
}