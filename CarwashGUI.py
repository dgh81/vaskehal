import customtkinter
from PIL import Image
import Carwash as carwash
from idlelib.tooltip import Hovertip

def main():
    global my_carwash
    my_carwash = carwash.Carwash()
    
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    global root
    root = customtkinter.CTk()
    root.geometry('1059')
    root.iconbitmap('./images/icon.ico')
    root.title('Vaskehallen')

    frame_root = customtkinter.CTkFrame(master=root)
    frame_root.pack(padx=60, pady=20, fill='both', expand=True)

    label_heading = customtkinter.CTkLabel(frame_root, text='Vaskehallen', font=('Ariel', 24))
    label_heading.pack(padx=60, pady=20)

    global frame_button_container
    frame_button_container = customtkinter.CTkFrame(frame_root)

    frame_button_container.columnconfigure(0, weight=1)
    frame_button_container.columnconfigure(1, weight=1)
    frame_button_container.columnconfigure(2, weight=1)
    frame_button_container.columnconfigure(3, weight=1)
    frame_button_container.columnconfigure(4, weight=1)


    #Række 1:
    btn_add_car = customtkinter.CTkButton(frame_button_container, text='Føj ny bil til kø', font=('Ariel', 16), command=add_car)
    btn_add_car.grid(row=1, column=0, padx=(10,10), pady=(10,10))
    
    global inputfield_licence_plate
    inputfield_licence_plate = customtkinter.CTkEntry(frame_button_container, placeholder_text='Nummerplade')
    inputfield_licence_plate.grid(row=1, column=1, padx=(10,10), pady=(10,10))

    global inputfield_owner
    inputfield_owner = customtkinter.CTkEntry(frame_button_container, placeholder_text='Ejer')
    inputfield_owner.grid(row=1, column=2, padx=(10,10), pady=(10,10))

    global car_categories
    car_categories = ['Kategori 1 (20 min)','Kategori 2 (30 min)','Kategori 3 (45 min)']

    global optionsmenu_categories
    optionsmenu_categories = customtkinter.CTkOptionMenu(frame_button_container, values=car_categories)
    optionsmenu_categories.grid(row=1, column=3)
    optionsmenu_categories.set("Kategori 1 (20 min)") #default


    # Række 2:
    btn_remove_first_car = customtkinter.CTkButton(frame_button_container, text='Fjern 1. bil i køen', font=('Ariel', 16), command=remove_first_car)
    btn_remove_first_car.grid(row=2, column=0, padx=(10,10), pady=(10,10))


    # Række 3:
    btn_show_car_cue_time = customtkinter.CTkButton(frame_button_container, text='Vis køtid', font=('Ariel', 16), command=show_car_cue_time)
    btn_show_car_cue_time.grid(row=3, column=0, padx=(10,10), pady=(10,10))

    global inputfield_licence_plate_for_cue_time
    inputfield_licence_plate_for_cue_time = customtkinter.CTkEntry(frame_button_container, placeholder_text='Nummerplade')
    inputfield_licence_plate_for_cue_time.grid(row=3, column=1, padx=(10,10), pady=(10,10))

    global label_cue_time
    label_cue_time = customtkinter.CTkLabel(frame_button_container, text='', font=('Ariel', 16))
    label_cue_time.grid(row=3, column=3, sticky=customtkinter.W+customtkinter.E)


    # Række 4:
    btn_remove_car = customtkinter.CTkButton(frame_button_container, text='Fjern bil', font=('Ariel', 16), command=remove_car)
    btn_remove_car.grid(row=4, column=0, padx=(10,10), pady=(10,10))

    global inputfield_licence_plate_for_remove_car
    inputfield_licence_plate_for_remove_car = customtkinter.CTkEntry(frame_button_container, placeholder_text='Nummerplade')
    inputfield_licence_plate_for_remove_car.grid(row=4, column=1, padx=(10,10), pady=(10,10))


    # Række 5:
    label_total_cue_time_header = customtkinter.CTkLabel(frame_button_container, text='Total køtid:', font=('Ariel', 16))
    label_total_cue_time_header.grid(row=5, column=0)

    global label_total_cue_time
    label_total_cue_time = customtkinter.CTkLabel(frame_button_container, text='0 min', font=('Ariel', 16))
    label_total_cue_time.grid(row=5, column=3)

    # Carframe:
    frame_button_container.pack(padx=60, pady=20, fill='both', expand=True)

    global carframe
    carframe = customtkinter.CTkFrame(master=root)
    carframe.columnconfigure(0, weight=1, uniform='row')
    carframe.columnconfigure(1, weight=1, uniform='row')
    carframe.columnconfigure(2, weight=1, uniform='row')
    carframe.columnconfigure(3, weight=1, uniform='row')
    carframe.columnconfigure(4, weight=1, uniform='row')
    carframe.columnconfigure(5, weight=1, uniform='row')
    carframe.columnconfigure(6, weight=1, uniform='row')
    carframe.columnconfigure(7, weight=1, uniform='row')
    carframe.columnconfigure(8, weight=1, uniform='row')
    
    label_temp = customtkinter.CTkLabel(master=carframe, image=customtkinter.CTkImage(Image.open("./images/empty.png"), size=(40,40)), text='')
    label_temp.grid(row=0, column=8, padx=(10,10), pady=(10,10))

    carframe.pack(padx=60, pady=20, side=customtkinter.BOTTOM, fill=customtkinter.BOTH, expand=False)

    root.mainloop()

def add_car():
    
    if len(inputfield_licence_plate.get()) < 8 and inputfield_owner.get() != '':
        
        if optionsmenu_categories.get() == car_categories[0]:
            car = carwash.CarCategori1(inputfield_owner.get(),inputfield_licence_plate.get())
            my_carwash.add_car(car)

        elif optionsmenu_categories.get() == car_categories[1]:
            car = carwash.CarCategori2(inputfield_owner.get(),inputfield_licence_plate.get())
            my_carwash.add_car(car)

        elif optionsmenu_categories.get() == car_categories[2]:
            car = carwash.CarCategori3(inputfield_owner.get(),inputfield_licence_plate.get())
            my_carwash.add_car(car)
        
        reset_add_car_fields()

    else:
        print("Nummerpladen er for lang eller ejeren mangler")
    
    show_total_cuetime()
    update_all_cars_in_cue()
    
def reset_add_car_fields():
    inputfield_licence_plate.delete('0', customtkinter.END)
    inputfield_owner.delete('0', customtkinter.END)
    optionsmenu_categories.set(car_categories[0])

def remove_first_car():
    my_carwash.remove_first_car()
    show_total_cuetime()
    label_cue_time.configure(text='')
    update_all_cars_in_cue()

def show_total_cuetime():
    total_time = ''
    if str(my_carwash.get_total_cue_time()) == None:
        total_time = '0 min'
    else:
        total_time = str(my_carwash.get_total_cue_time()) + ' min'
    label_total_cue_time.configure(text=str(total_time))

def show_car_cue_time():
    cue_time = ''
    if my_carwash.get_car_cue_time(inputfield_licence_plate_for_cue_time._placeholder_text) != None:
        cue_time = str(my_carwash.get_car_cue_time(inputfield_licence_plate_for_cue_time._placeholder_text)) + ' min'
    else:
        cue_time = '0 min'
    label_cue_time.configure(text=cue_time)

def remove_car():
    my_carwash.remove_car(inputfield_licence_plate_for_remove_car._placeholder_text)
    inputfield_licence_plate_for_remove_car.delete('0', customtkinter.END)
    inputfield_licence_plate_for_cue_time.delete('0', customtkinter.END)
    label_cue_time.configure(text='')

    show_total_cuetime()
    update_all_cars_in_cue()

def update_all_cars_in_cue():

    # oprydning af gamle imageLabels:
    for label in carframe.grid_slaves():
        label.grid_forget()

    for index,car in enumerate(my_carwash.car_list):

        # populate car image grid kø:
        if index <= 8:
            image_car = car.getImage()
            if index == 0:
                label_container_for_car_image = customtkinter.CTkLabel(master=carframe, image=image_car, text='', bg_color='#446699')
            else:
                label_container_for_car_image = customtkinter.CTkLabel(master=carframe, image=image_car, text='')
            Hovertip(label_container_for_car_image,'Nummerplade: ' + car.licence_plate + '\n' + 'Ejer: ' + car.owner)  
            label_container_for_car_image.grid(row=0, column=8-index, padx=(10,10), pady=(10,10))
            label_container_for_car_image.bind("<Button-1>", lambda event, arg=car: car_clicked_event(event, arg))     

def car_clicked_event(event, widget):
    inputfield_licence_plate_for_cue_time.configure(placeholder_text=widget.licence_plate)
    inputfield_licence_plate_for_remove_car.configure(placeholder_text=widget.licence_plate)

if __name__ == '__main__':
    main()