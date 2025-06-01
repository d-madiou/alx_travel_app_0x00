#!/usr/bin/env python3
"""Models for listings app."""

from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Listing(models.Model):
    """
    Represents a rental listing.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Booking(models.Model):
    """
    Represents a booking for a listing.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Booking by {self.user} for {self.listing}"

class Review(models.Model):
    """
    Represents a review for a listing.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user} for {self.listing}"
