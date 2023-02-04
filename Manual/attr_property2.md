* Products
    1. Product
        * fields
            1. id
            2. name
            3. slug
            4. short_description
            5. description
            6. gender
            7. is_available
            8. is_delete
            9. deleted_on
            10. modified_at
            11. created_at

            * comments
            * category/categorys
            * tag/tags
            * brand/brands
            * inventory_items
            * gallery
            * favorite_items
            * wishlist_items
        * properties
            * category_count
            * category_object
            * category_name
            * brand_count
            * brand_object
            * brand_name
            * tag_count
            * tag_object
            * tag_name
            * comment_count
            * comment_object
            * rating
            * inventory_itme_object
            * inventory_itme_count
            * inventory_item_market
            * inventory_item_min_price
            * inventory_item_max_price
            * inventory_item_average_price
            * inventory_item_has_discount
            * favorite_count
            * wishlist_count
            * seller_count
            * all_offers
            * best_offer
            * images
            * primary_image
        * functions
            * get_absolute_url
              path :/product/detail/<slug:slug>/
            * str
              self.name
            * slug
              self.name
        * signal
            * pre_save
              self.slug = slugify(self.name)
              initial_pre_save("name": instance.name)
            * post_save
              check_gallery
              Product.category.through:update category ancenstor
    2. Brand
        * fields
            1. id
            2. name
            3. slug
            4. description
            5. is_delete~~~~
            6. deleted_on
            7. modified_at
            8. created_at

            * product/products
            * gallery
        * properties
            * product_count
            * product_object
            * product_name
            * category_count
            * category_object
            * category_name
            * tag_count
            * tag_object
            * tag_name
            * comment_count
            * comment_object
            * rating
            * inventory_itme_object
            * inventory_itme_count
            * inventory_item_market
            * favorite_count
            * wishlist_count
            * sell_count
            * images
            * primary_image
        * functions
            * get_absolute_url
              path :/brand/<slug:slug>/
            * str
              self.name
            * slug
              self.name
            * signal
                * pre_save
                  self.slug = slugify(self.name)
                  initial_pre_save("name": instance.name)
                * post_save
                  check_gallery
                  update_images
    3. Category
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
        * signal
            * pre_save
            * post_save
    4. Tag
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    5. Comment
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
* Customers
    1. Customer
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    2. Cart
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    3. CartItem
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    4. CustomerCoupon
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    5. Coupon
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    6. Favorite
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    7. FavoriteItem
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    8. OrderCustomer
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    9. WishList
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
    10. WishListItem
        * fields
            1. id
            2. ?

            * ?
        * properties
            * ?
        * functions
            * get_absolute_url
              path :?
            * str
              ?
            * slug
              ?
            * signal
                * pre_save
                * post_save
* Markets
    1. Market
    2. Inventory
    3. InventoryItem
    4. InventoryItemPropertyItem
    5. PropertyItem
    6. OrderMarket
* Shops
    1. Address
    2. Discount
    3. Gallery
    4. Image
    5. GalleryImage
    6. Order
    7. OrderItem
    8. Payment
    9. Wallet
    10. Shipment
    11. ContactUs
* Users
    * User