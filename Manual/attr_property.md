Products


    Product
        id



        name
        slug
        short_description
        description
        gender
        is_available
        is_delete
		deleted_on
        modified_at
        created_at
            comment
            category
            tag
            brand
            inventory_item
            gallery
            favorite
            wishlist
        category_count
        category_object
        category_name
        brand_count
        brand_object
        brand_name
        tag_count
        tag_object
        tag_name
        comment_count
        comment_object
        rating
        inventory_itme_object
        inventory_itme_count
        inventory_item_market
        inventory_item_min_price
        inventory_item_max_price
        inventory_item_average_price
        inventory_item_has_discount
        favorite_count
        wishlist_count
        seller_count
        all_offers
        best_offer
        images
        primary_image


    *
        * get_absolute_url
            path :/product/detail/<slug:slug>/
        * str
            self.name
        * slug
            self.name


    # signal
        pre_save
            self.slug = slugify(self.name)
            initial_pre_save("name": instance.name)
        post_save
            check_gallery
            Product.category.through:update category ancenstor


    Brand
        id



        name
        slug
        description
        is_delete
		deleted_on
        modified_at
        created_at
            product
            gallery
        product_count
        product_object
        product_name
        category_count
        category_object
        category_name
        tag_count
        tag_object
        tag_name
        comment_count
        comment_object
        rating
        inventory_itme_object
        inventory_itme_count
        inventory_item_market
        favorite_count
        wishlist_count
        sell_count
        images
        primary_image


    *
        * get_absolute_url
            path :/brand/<slug:slug>/
        * str
            self.name
        * slug
            self.name


    # signal
        pre_save
            self.slug = slugify(self.name)
            initial_pre_save("name": instance.name)
        post_save
            check_gallery
            update_images


    Category
        id



        name
        slug
        description
        is_delete
		deleted_on
        modified_at
        created_at
            parent
            product
            gallery
        parent_object
        parent_name
        parent_slug
        parent_count
        parent_slug
        child_object
        child_name
        child_count
        product_count
        product_object
        product_name
        brand_count
        brand_object
        brand_name
        tag_count
        tag_object
        tag_name
        comment_count
        comment_object
        rating
        inventory_itme_object
        inventory_itme_count
        inventory_item_market
        favorite_count
        wishlist_count
        sell_count
        images
        primary_image


    *
        * get_absolute_url
            path :/category/<slug:slug>/
        * str
            self.name
        * slug
            self.name+parent.names


    #
        pre_save
            self.slug = slugify(self.name)
            instance = check_parent(instance)
            instance = check_childs(instance)
            initial_pre_save("name": instance.name)
        post_save
            check_gallery(instance)
            update_images(instance)
            instance = slug_from_parent(instance)
            instance = update_childs(instance)
            update_products(instance)


    Tag
        id



        name
        slug
        description
        is_delete
		deleted_on
        modified_at
        created_at
            product
            gallery
        product_count
        product_object
        product_name
        category_count
        category_object
        category_name
        brand_count
        brand_object
        brand_name
        comment_count
        comment_object
        rating
        inventory_itme_object
        inventory_itme_count
        inventory_item_market
        favorite_count
        wishlist_count
        sell_count
        images
        primary_image


    *
        * get_absolute_url
            path :/tag/<slug:slug>/
        * str
            self.name
        * slug
            self.name


    # signal
        pre_save
            self.slug = slugify(self.name)
            initial_pre_save("name": instance.name)
        post_save
            check_gallery
            update_images


    Comment
        id



        title
        body
        rating
        is_delete
		deleted_on
        modified_at
        created_at
            product
            author:customer
            gallery
        product_object
        product_name
        brand_name
        category_name
        author_object
        author_name
        tag_name


    *
        * get_absolute_url
            path :/comment/<slug:slug>/
        * str
            self.title
        * slug
            self.id





    # signal
        pre_save
            self.slug = slugify(self.id


)
            initial_pre_save("name": instance.id


)
        post_save
            check_gallery
Customers


    Customer
        id



        firstname
        lastname
        user_name
        slug
        gender
        email
        bio
        is_delete
		deleted_on
        modified_at
        created_at
            gallery
            comment
            user
            wishlist
            favorite
            wallet
            address
            cart
            coupon
            order_customer
        full_name
        primary_image
        images
        comment_object
        comment_count
        wish_list_object
        wish_list_count
        favorite_object
        favorite_count
        address_object
        address_count
        cart_object
        cart_count
        coupon_object
        coupon_object_used
        coupon_object_unused
        order_customer_object
        order_customer_count
        order_history
        order_pending
        order_finished


    *
        * get_absolute_url
            path :/customer/<slug:slug>/
        * str
            self.user_name
        * slug
            self.user_name


    # signal
        pre_save
            maker_user_name
            slug = user_name
        post_save
            check_gallery


    Cart
        id



        is_delete
		deleted_on
        modified_at
        created_at
            cart_item
            customer
        cart_item_object
        cart_item_count
        customer_object
        customer_user_name
        cart_item_inventory_item
        cart_item_product
        cart_item_images


    CartItem
        id



        is_delete
		deleted_on
        modified_at
        created_at
        
            cart
            inventory_item
        cart_object
        cart_customer_object
        inventory_item_object
        inventory_object
        market_object
        product_object
        primary_image


    CustomerCoupon
        id



        is_used
        is_delete
		deleted_on
        modified_at
        created_at
            customer_id



            coupon_id



            order_id



        customer_object
        coupon_object
        order_customer_object
        order_object


    Coupon
        id
        
        date_from
        date_to
        code
        coupon_type
        minimum_amount
        maximum_amount
        percentage
        is_tax_free
        is_shipping_free
            customer

        is_delete
		deleted_on
        modified_at
        created_at


    Favorite
        id
            customer
            favorite_item


        is_delete
		deleted_on
        modified_at
        created_at


    FavoriteItem
        id
        
            favorite
            product

        is_delete
		deleted_on
        modified_at
        created_at


    OrderCustomer
        id

        Status_order
        total_price
        tax
        discounted_price
        final_price
    
            order
            order_item
            shipment
            payment
            coupon
            customer

        is_delete
		deleted_on
        modified_at
        created_at


    WishList
        id

            wish_list_item
            customer


        is_delete
		deleted_on
        modified_at
        created_at


    WishListItem
        id
        
            wish_list
            product
        

        is_delete
		deleted_on
        modified_at
        created_at
Markets


    Market
        id
    
        firstname
        lastname
        user_name
        slug
        email
        bio
            user
            gallery
            wallet
            inventory
            address
            order_market

        is_delete
		deleted_on
        modified_at
        created_at
    


    Inventory
        id
    
        date_open
        date_close
        time_open
        time_close
        weekdays
            market
            inventory_item

        is_delete
		deleted_on
        modified_at
        created_at
    


    InventoryItem
        id

        price
        date_from
        date_to
        time_from
        time_to
        weekdays
            inventory
            discount
            product
            cart_item
            order_item
            property_item


        is_delete
		deleted_on
        modified_at
        created_at
    


    InventoryItemPropertyItem
        id

            inventoryitem_id
            propertyitem_id


        is_delete
		deleted_on
        modified_at
        created_at
    


    PropertyItem
        id


        key
        value
            inventory_item

        is_delete
		deleted_on
        modified_at
        created_at
    


    Ordermarket
        id

        status_order
        total_price
        status_payment
            order_item
            order
            shipment
            payment
            market

        is_delete
		deleted_on
        modified_at
        created_at
    
Shops


    Address
        id


        country
        city
        province
        address_line
        postal_code
        firstname
        lastname
        coordinate
        slug
    
            content_type
            object_id
            object
    
        is_delete
		deleted_on
        modified_at
        created_at
    


    Discount
        id

        discount_type
        minimum_amount
        maximum_amount
        percentage
        date_from
        date_to
            inventory_item


        is_delete
		deleted_on
        modified_at
        created_at
    


    Gallery
        id

            image
            content_type
            object_id
            object

        is_delete
		deleted_on
        modified_at
        created_at
    


    Image
        id
        
        name
        path_original
        path_thumbnail
        image
        image_thumbnail
        alt_text
            gallery


        is_delete
		deleted_on
        modified_at
        created_at
    


    GalleryImage
        id

            gallery_id
            image_id


        is_delete
		deleted_on
        modified_at
        created_at
    


    Order
        id


        status_order
            order_item
            order_customer
            order_market

        is_delete
		deleted_on
        modified_at
        created_at
    


    OrderItem
        id

        quantity
        final_price
            order
            order_customer
            inventory_item
            order_market


        is_delete
		deleted_on
        modified_at
        created_at
    


    Payment
        id

        payment_type
        amount
        description
        status_payment
            content_type
            object_id
            object


        is_delete
		deleted_on
        modified_at
        created_at
    


    Wallet
        id

        amount
        sheba
        card_number
        firstname
        lastname
    
            content_type
            object_id
            object

        is_delete
		deleted_on
        modified_at
        created_at
    


    Shipment
        id

        shipment_type
        status_shipment
            order_customer
            order_market

        is_delete
		deleted_on
        modified_at
        created_at
    


    ContactUs
        id

        firstname
        lastname
        title
        body
        email

        is_delete
		deleted_on
        modified_at
        created_at
Users


    User
        id

        phone_number
    
        is_customer
            customer
        is_market
            market
        is_staff
    
        is_active
    
        is_admin
    
        is_superuser
    
        is_verified
    
        slug

        is_delete
		deleted_on
        modified_at
        created_at
    