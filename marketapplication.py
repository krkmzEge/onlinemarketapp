while True:
    print('Welcome to the Losso Market App')
    print('Please Log In:')
    
    username = input ('Username...:')
    password = input ('Password...:')

    print('Welcome', username, 'good afternoon.')
    
    
    print('Fruit&Veg (FV)')
    print('Meats   (M)')
    print('Fishes  (F)')
    print('Alcohol (A)')
    print('Crisps&Snakcs (CS)')
    print('Soft Drinks (S)')
    print('Ready Meals (R)')
    print('Bakery  (B)')
    
    choice = input(":")
    
    if choice == 'FV':
        
        print('Red Apple 2,99$kg (1)')
        print('Avocado 4,99$per (2)')
        print('Banana 3,50$kg (3)')
        print('Blueberrie 7,99$(500gr) (4)')
        print('Broccoli 8,99$per (5)')
        print('Carrot 4,99$kg (6')
        print('Eggplant 4,99$kg (7)')
        print('Grape 6,79$kg (8)')
        print('Garlic 2,99$per (9)')
        print('Ginger 5,59$kg (10)')
        print('Iceberg 7,99$kg (11)')
        print('Lettuce 8,99$kg (12)')
        print('Kiwi 5,99$kg (13)')

        choice = input(":")
        if choice == '1':
            print('Added to basket! (1kg)')
        if choice == '2':  
            print('Added to basket! (1per)') 
        if choice == '3':   
            print('Added to basket! (1kg)')
        if choice == '4':  
            print('Added to basket! (500gr)')
        if choice == '5': 
            print('Added to basket! (1per)')  
        if choice == '6':
            print('Added to basket! (1kg)')
        if choice == '7':
            print('Added to basket! (1kg)')
        if choice == '8':
            print('Added to basket! (1kg)')
        if choice == '9':
            print('Added to basket! (1per)')
        if choice == '10':
            print('Added to basket! (1kg)')
        if choice == '11':
            print('Added to basket! (1kg)')
        if choice == '12':
            print('Added to basket! (1kg)')
        if choice == '13':
            print('Added to basket! (1kg)')
                        
    if choice == 'M':
        
        print('%73 Lean Ground Beef 19,99$ 1kg (1)')
        print('%80 Lean Ground Beef 20,99$ 1kg (2)')
        print('%80 Lean Ground Beef 22,99$ 1kg (3)')
        print('%85 Lean Ground Beef 25,99$ 1kg (4)')
        print('%90 Lean Ground Beef Sirloin 27,99$ 1kg (5)')

        choice = input(":")
        if choice == '1':
            print('Added to basket! (1kg)')
        if choice == '2':    
            print('Added to basket! (1kg)')
        if choice == '3':    
            print('Added to basket! (1kg)')
        if choice == '4':    
            print('Added to basket! (1kg)')
        if choice == '5':    
            print('Added to basket! (1kg)')
    
    if choice == 'F':
        print('Fresh Atlantic Salmon 29,99$ 1kg (1)')
        print('Fresh Steelhead Trout 27,99$ 1kg (2)')
        print('Fresh Tilapia with Garlic Herb 37,99$ 1per (3)')

        choice = input(":")
        if choice == '1':
            print('Added to basket! (1kg)')
        if choice == '2':
            print('Added to basket! (1kg)')
        if choice == '3':
            print('Added to basket! (1per)')

    if choice == 'A':
        print('Red Wine (R):')
        print('White Wine (W):')
        print('Sparkling Wine (S):')
        print('Rosé Wine (RO):')
        print('Specialty Wine (SPE):')
        print('Beer (B):')

        choice = input(":")
        if choice == 'R':
            print('William Wright Reserve Pinot Noir 49,99$ (1)')
            print('Bear Bros. Cabernet Sauvignon 55,89$ (2)')
            print('Bridge Road Vineyards Cabernet Sauvignon 79,80$ (3)')
            print('Winking Owl Cabernet Sauvignon 69,99$ (4) ')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')
        
        if choice == 'W':
            print('William Wright Chardonnay 39,99$ (1)')
            print('Essenza di Vita Pinot Grigio 56,99$ (2)')
            print('Exquisite Collection Chardonnay 45,99$ (3)')
            print('Giretto Pinot Grigio 42,99$ (4)')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')

        if choice == 'S':
            print('Belletti Sparkling Moscato Rosé 35,99$ (1):')
            print('Burlwood Cellars Extra Dry Sparkling 38,99$ (2)')
            print('Burlwood Brut Sparkling 32,99$ (3)')
            print('Giambellino Peach Bellini 37,99$ (4)')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')

        if choice == 'RO':
            print('Bridge Road Vineyards White Zinfandel 45,99$ (1)')
            print('Exquisite Collection Côtes de Provence Rosé 42,99$ (2)')
            print('Trestoria Rosé 40,99$ (3)')
            print('Moiselle Pink Moscato 37,99$ (4)')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')

        if choice == 'SPE':
            print('Connellys Original Country Cream 59,99$ (1)')
            print('Pacific Fruit Vineyards Sweet Peach Wine 37,99$ (2)')
            print('Pacific Fruit Vineyards Sweet Pineapple Wine 37,99$ (3)')
            print('Petit Chocolat Wine Specialty 29,99$ (4)')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')

        if choice == 'B':
            print('Hopping Nomad Session IPA 18,99$ (1)')
            print('Holland Lager 1839 22,99$ (2)')
            print('Monterrey Cerveza 15,99$ (3)')
            print('Wernesgrüner Pilsner 12,99$ (4)')

            choice = input(":")
            if choice == '1':
               print('Added to basket!')
            if choice == '2':
               print('Added to basket!')
            if choice == '3':
               print('Added to basket!')
            if choice == '4':
               print('Added to basket!')
        
    if choice == 'CS': 
        print('Pepperidge Farm Goldfish Original 3,99$ (1)')
        print('Clancys Wavy Potato Chips 2,99$ (2)')
        print('Simply Nature Organic Blue Corn Tortilla Chips 4,99$ (3)')
        print('Savoritz Golden Rounds 4,99$ (4)')
        print('Moser Roth Dark Collection 70% 2,99$ (5)')
        print('Choceur Dark Chocolate 3,99$ (6)')
        print('Specially Selected Dark Chocolate Coated Butter Cookies 5,99$ (7)')
        print('Bentons Peanut Butter Filled Cookies 3,99$ (8)')
        print('Southern Grove Deluxe Mixed Nuts with Sea Salt 8,99$ (9)')
        print('Southern Grove Pistachios 6,99$ (10)')
        print('Southern Grove Pumpkin Seeds 5,99$ (11)')
        print('Simply Nature Raw Almonds, Pecans, and Pistachio Kernels 9,99$ (12)')
        print('Lunch Buddies Fruit Flavored Snacks Assorted Flavors 6,99$ (13)')
        print('Simply Nature Freeze Dried Fuji Apples 8,99$ (14)')
        print('Simply Nature Fruit Strips Strawberry 8,99$ (15)')

        choice = input(":")
        if choice == '1':
               print('Added to basket!')
        if choice == '2':
               print('Added to basket!')
        if choice == '3':
               print('Added to basket!')
        if choice == '4':
               print('Added to basket!')
        if choice == '5':
               print('Added to basket!')
        if choice == '6':
               print('Added to basket!')
        if choice == '7':
               print('Added to basket!')
        if choice == '8':
               print('Added to basket!')
        if choice == '9':
               print('Added to basket!')
        if choice == '10':
               print('Added to basket!')
        if choice == '11':
               print('Added to basket!')
        if choice == '12':
               print('Added to basket!')
        if choice == '13':
               print('Added to basket!')
        if choice == '14':
               print('Added to basket!')
        if choice == '15':
               print('Added to basket!')
                                                         
    if choice == 'S':
        print('7up 330ml 1,99$ (1)')
        print('Acti-Vit Sparkling Vitamin Water Tropical Mango, Pineapple & Passion Fruit 330ml 2,50$ (2)')
        print('Coca-Cola 330ml 1,99$ (3)')
        print('Caffeine Free Coca-Cola 2,50$ (4)')
        print('Coca-Cola Cherry 2,50$ (5)')
        print('Fanta 330ml 1,50$ (6)')
        print('Sprite 330ml 1,99$ (7)')
        print('Gatorade 500ml 3,50$ (8)')
        print('Mountain Dew 330ml 2,50$ (9)')
        print('Mountain Dew 500ml 3,50$ (10)')
        print('Pepsi 330ml 1,99$ (11)')
        print('Dr Pepper 330ml 1,99$ (12)')

        choice = input(":")
        if choice == '1':
               print('Added to basket!')
        if choice == '2':
               print('Added to basket!')
        if choice == '3':
               print('Added to basket!')
        if choice == '4':
               print('Added to basket!')
        if choice == '5':
               print('Added to basket!')
        if choice == '6':
               print('Added to basket!')
        if choice == '7':
               print('Added to basket!')
        if choice == '8':
               print('Added to basket!')
        if choice == '9':
               print('Added to basket!')
        if choice == '10':
               print('Added to basket!')
        if choice == '11':
               print('Added to basket!')
        if choice == '12':
               print('Added to basket!')       
    
 
    if choice == 'R':
        print('Heat & Go BBQ Pulled Pork Burrito 249g 4,99$ (1)')
        print('Heat & Go Vegan Chilli Non Carne Burrito 249g 4,99$ (2)')
        print('Eat & Go Smoked Salmon & Soft Cheese Sandwich 184g 3,99$ (3)')
        print('The Deli Smoked Pork Sausage 260g 3,99$ (4)')
        print('Heat & Go Vegan Chilli Non Carne Burrito 249g 3,99$ (5)')
        print('Plant Menu Spicy Veggie Wrap 188g 3,99$ (6)')
        print('Eat & Go BBQ Chicken & Bacon Wrap 188g 3,99$ (7)')
        print('Eat & Go Peri Peri Chicken Wrap 188g 3,99$ (8)')
        print('Eat & Go Turkey Feast Wrap 202g 4,99$ (9)')

        choice = input(":")
        if choice == '1':
               print('Added to basket!')
        if choice == '2':
               print('Added to basket!')
        if choice == '3':
               print('Added to basket!')
        if choice == '4':
               print('Added to basket!')
        if choice == '5':
               print('Added to basket!')
        if choice == '6':
               print('Added to basket!')
        if choice == '7':
               print('Added to basket!')
        if choice == '8':
               print('Added to basket!')
        if choice == '9':
               print('Added to basket!')

    if choice == 'B':
        print('Village Bakery Super Soft Original Wraps 8 Pack 1,50$ (1)')
        print('Village Bakery Toastie Thick Sliced White Bread 800g 1,50$ (2)')
        print('Specially Selected Sliced Brioche Burger Buns 200g/4 Pack 1,99$ (3)')
        print('Hovis Soft White Medium 800g 2,50$ (4)')
        print('Village Bakery Toasting Waffles 250g/12 Pack 2,39$ (5)')
        print('Hovis Best Of Both Medium 750g 2,39$ (6)')
        print('Specially Selected Sliced Seeded Brioche Burger Buns 200g/4 Pack 2,29$ (7)')

        choice = input(":")
        if choice == '1':
               print('Added to basket!')
        if choice == '2':
               print('Added to basket!')
        if choice == '3':
               print('Added to basket!')
        if choice == '4':
               print('Added to basket!')
        if choice == '5':
               print('Added to basket!')
        if choice == '6':
               print('Added to basket!')
        if choice == '7':
               print('Added to basket!')
        

        
        break 