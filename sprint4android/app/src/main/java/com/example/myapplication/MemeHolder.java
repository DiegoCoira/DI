package com.example.myapplication;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class MemeHolder extends RecyclerView.ViewHolder{
    private TextView name;
    private ImageView game;

    public MemeHolder(@NonNull View ivi) {
        super(ivi);
        name = ivi.findViewById(R.id.text_view_game);
        game = ivi.findViewById(R.id.image_view_game);
    }

    public void showData(Memes memeData) {
        this.name.setText(memeData.getName());
        DownloadImg.downloadBitmapToImageView(memeData.getImage_url(), this.game);
    }
}
