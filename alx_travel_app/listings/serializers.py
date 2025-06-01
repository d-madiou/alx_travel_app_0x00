#!/usr/bin/env python3
"""Serializers for listings app."""

from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for listing model.
    """
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'owner', 'location']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for booking model.
    """
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date']
