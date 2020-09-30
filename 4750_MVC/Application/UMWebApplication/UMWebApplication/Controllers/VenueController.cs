using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using UMWebApplication.Models;

namespace UMWebApplication.Controllers
{
    public class VenueController : Controller
    {
        // GET: Venue
        public ActionResult Index()
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.venues.ToList());
            }
        }

        // GET: Venue/Details/5
        public ActionResult Details(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.venues.Where(x => x.venueID == id).FirstOrDefault());
            }
        }

        // GET: Venue/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Venue/Create
        [HttpPost]
        public ActionResult Create(venue v)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    ab.venues.Add(v);
                    ab.SaveChanges();
                    
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Venue/Edit/5
        public ActionResult Edit(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.venues.Where(x => x.venueID == id).FirstOrDefault());
            }
        }

        // POST: Venue/Edit/5
        [HttpPost]
        public ActionResult Edit(int? id, venue v)
        {
            try
            {
                using (UMWEBDBEntities1 a = new UMWEBDBEntities1())
                {
                    a.Entry(v).State = EntityState.Modified;
                    a.SaveChanges();
                }
                // TODO: Add update logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Venue/Delete/5
        public ActionResult Delete(int? id)
        {
            using (UMWEBDBEntities1 b = new UMWEBDBEntities1())
            {
                return View(b.venues.Where(x => x.venueID == id).FirstOrDefault());
            }
        }

        // POST: Venue/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {

                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    venue vo = ab.venues.Where(x => x.venueID == id).FirstOrDefault();
                    ab.venues.Remove(vo);
                    ab.SaveChanges();
                }
                // TODO: Add delete logic here

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
