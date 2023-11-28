package com.example.myapplication;


import org.json.JSONException;
import org.json.JSONObject;
public class Memes {
    private String name;
    private String description;
    private String image_url;

    public String getName() {return name;}
    public String getDescripcion() {return description;}
    public String getImage_url() {return image_url;}

    public Memes(JSONObject json){
        try{
            this.name = json.getString("name");
            this.description = json.getString("description");
            this.image_url = json.getString("image_url");
        }catch (JSONException e){ e.printStackTrace(); }
    }
}
