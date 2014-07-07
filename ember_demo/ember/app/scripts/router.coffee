EmberApp.Router.map ->
  # Add your routes here
  @.route('about')
  @.resource('products', ->
    this.resource('product', {path: "/:product_id"})
    this.route('onSale')
    )
