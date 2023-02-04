

    5. GalleryImage
        * fields
            1. Gallery\foreign key\related_name=gallery_images
            2. Image\foreign key\related_name=gallery_images
        * rels

    6. Order
        * fields
            1. OrderCustomer\onetotone\related_name=orders
            2. OrderMarket\foreign key\related_name=orders
        * rels
            1. OrderItem\foreign key\related_name=orders

    7. OrderItem
        * fields
            1. InventoryItem\foreign key\related_name=order_items
            2. Order\foreign key\related_name=order_items
            3. OrderCustomer\foreign key\related_name=order_items
            4. OrderMarket\foreign key\related_name=order_items
        * rels

    8. Payment
        * fields
            1. generics + owner def
        * rels

    9. Wallet
        * fields
            * generics + owner def
        * rels

    10. Shipment
        * fields
        * rels
            1. OrderCustomer\foreign key\related_name=shipments
            2. OrderMarket\foreign key\related_name=shipments


