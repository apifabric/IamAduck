import { MenuRootItem } from 'ontimize-web-ngx';

import { AddresCardComponent } from './Addres-card/Addres-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { ItemCardComponent } from './Item-card/Item-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderStatuCardComponent } from './OrderStatu-card/OrderStatu-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProductPromotionCardComponent } from './ProductPromotion-card/ProductPromotion-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplierProductCardComponent } from './SupplierProduct-card/SupplierProduct-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Addres', name: 'ADDRES', icon: 'view_list', route: '/main/Addres' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Item', name: 'ITEM', icon: 'view_list', route: '/main/Item' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderStatu', name: 'ORDERSTATU', icon: 'view_list', route: '/main/OrderStatu' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'ProductPromotion', name: 'PRODUCTPROMOTION', icon: 'view_list', route: '/main/ProductPromotion' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplierProduct', name: 'SUPPLIERPRODUCT', icon: 'view_list', route: '/main/SupplierProduct' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AddresCardComponent

    ,CustomerCardComponent

    ,ItemCardComponent

    ,OrderCardComponent

    ,OrderStatuCardComponent

    ,PaymentCardComponent

    ,ProductCardComponent

    ,ProductPromotionCardComponent

    ,PromotionCardComponent

    ,ReviewCardComponent

    ,SupplierCardComponent

    ,SupplierProductCardComponent

];