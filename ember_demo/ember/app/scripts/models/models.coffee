EmberApp.Product = DS.Model.extend({
    title: DS.attr('string'),
    price: DS.attr(),
    description: DS.attr(),
    isOnSale: DS.attr(),
    image: DS.attr(),
    reviews: DS.hasMany('review', {async: true}),
});

EmberApp.Review = DS.Model.extend({
    text: DS.attr('string'),
    reviewedAt: DS.attr('date'),
    product: DS.belongsTo('product')
});
