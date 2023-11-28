package com.example.myapplication;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;


import java.util.List;

public class MemesRecicleViewAdapter extends RecyclerView.Adapter<MemesRecicleViewAdapter.MyViewHolder> {

    private final List<Memes> memesList;
    private final Context context;

    public MemesRecicleViewAdapter (List<Memes> memesList, Activity activity) {
        this.memesList = memesList;
        this.context = activity;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.view_meme_cell, parent, false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        Memes  item = memesList.get(position);

        holder.itemTitle.setText(item.getName());
        Glide.with(context).load(item.getImage_url()).into(holder.itemImage);

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Al hacer clic en la celda, abrir la DetailActivity y pasar los datos
                Intent intent = new Intent(context, DetailActivity.class);
                intent.putExtra("name", item.getName());
                intent.putExtra("image_url", item.getImage_url());
                intent.putExtra("description", item.getDescripcion());
                context.startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return memesList.size();
    }

    public static class MyViewHolder extends RecyclerView.ViewHolder {
        ImageView itemImage;
        TextView itemTitle;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            itemImage = itemView.findViewById(R.id.itemImageView);
            itemTitle = itemView.findViewById(R.id.itemNameTextView);
        }
    }
}