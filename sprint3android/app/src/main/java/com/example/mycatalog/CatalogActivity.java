package com.example.mycatalog;

import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    private DrawerLayout drawerLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);

        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
             super.onBackPressed();
        }
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {

        int titleId = getTitle(menuItem);

        showFragment(titleId);

        drawerLayout.closeDrawer(GravityCompat.START);

        return true;
    }

    private int getTitle(@NonNull MenuItem menuItem) {
        String itemId = (String) menuItem.getTitle();

        if (itemId.equals("Catalog")) {
            return R.string.CatalogFragment;
        } else if (itemId.equals("About")) {
            return R.string.AboutFragment;
        }
        return 0;
    }

    private void showFragment(@StringRes int titleId) {
        Fragment fragment;
        if (titleId == R.string.CatalogFragment) {
            fragment = CatalogFragment.newInstance();
            getSupportFragmentManager().beginTransaction().replace(R.id.home_content, fragment).commit();
            setTitle(getString(titleId));
        }

        else if (titleId == R.string.AboutFragment){
            fragment = AboutFragment.newInstance();
            getSupportFragmentManager().beginTransaction().replace(R.id.home_content, fragment).commit();
            setTitle(getString(titleId));
        }
    }
}
