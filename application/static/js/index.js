const btnCart = document.querySelector('.container-icon')
const containerCartProducts = document.querySelector('.container-cart-products')

btnCart.addEventListener('click', () => {
    containerCartProducts.classList.toggle('hidden-cart')
})


var productos = [];

function addProduct(producto){
    productos.push(producto)
    renderCart()
}

function removeProduct(index){
    productos.splice(index-1, 1)
    renderCart()
}


function renderCart(){
    var cart = document.getElementById("product-car");
    cart.innerHTML = "";
    
    productos.forEach(function callback(pro, index, array) {
        pro = {...pro}
        pro.index = index+1;
        let node = createProductNode(pro);
        cart.appendChild(node);
    });
    cart.appendChild(createTotalNode());

    var contador = document.getElementById("contador-productos")
    contador.innerText = productos.length
}


function createProductNode(producto){
    const {index, nombre, precio} = producto

    var product = document.createElement("div");
    product.classList.add("cart-product");
    product.innerHTML = `
        <div class="info-cart-product">
            <span class="cantidad-producto-carrito">${index}</span>
            <p class="titulo-producto-carrito">${nombre}</p>
            <span class="precio-producto-carrito">$${precio}</span>
        </div>
    `

    var icon = document.createElement("div");
    icon.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="icon-close">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
    `
    icon.addEventListener("click", (e)=>{
        e.stopPropagation();
        removeProduct(index)
    }, )

    product.appendChild(icon)
    return product
}

function createTotalNode(){
    var total = productos.reduce((accumulator, currentValue) => accumulator + currentValue.precio, 0);
    
    var cartTotal = document.createElement("div");
    cartTotal.classList.add("cart-total")
    cartTotal.innerHTML = `
        <h3>Total:</h3>
        <span class="total-pagar">$${total}</span>
    `;
    return cartTotal
}