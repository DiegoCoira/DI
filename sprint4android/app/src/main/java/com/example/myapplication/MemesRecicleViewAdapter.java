package com.example.myapplication;

import android.app.Activity;
import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.myapplication.Memes;
import com.example.myapplication.R;

import java.util.List;

public class MemesRecicleViewAdapter extends RecyclerView.Adapter<MemesRecicleViewAdapter.MyViewHolder> {

    private final List<Memes> memesList;
    private final Context context;

    public MemesRecicleViewAdapter(List<Memes> memesList, Activity activity) {
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
        Memes item = memesList.get(position);

        holder.Title.setText(item.getName());
        holder.Description.setText(item.getDescripcion());

        Glide.with(context).load(item.getImage_url()).into(holder.Image);

        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });
    }

    @Override
    public int getItemCount() {
        return memesList.size();
    }

    public static class MyViewHolder extends RecyclerView.ViewHolder {
        ImageView Image;
        TextView Title;
        TextView Description;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            Image = itemView.findViewById(R.id.itemImageView);
            Title = itemView.findViewById(R.id.itemNameTextView);
            Description = itemView.findViewById(R.id.itemDescriptionTextView);
        }
    }

}