package com.example.myapplication;


import org.json.JSONException;
import org.json.JSONObject;
public class Memes {
    private String name;
    private String descripcion;
    private String image_url;

    public String getName() {return name;}
    public String getDescripcion() {return descripcion;}
    public String getImage_url() {return image_url;}

    public Memes(JSONObject json){
        try{
            this.name = json.getString("name");
            this.descripcion = json.getString("descripcion");
            this.image_url = json.getString("image_url");
        }catch (JSONException e){ e.printStackTrace(); }
    }
}
